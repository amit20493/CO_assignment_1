from os import error, linesep
import OpcodeTable as op
import Symboltable
import error_type
import sys
from sys import stdin


def getLineIndex(line):
    return original_file_list.index(line)+1

def to8bitBinary(location):
    locationInBinary=bin(location).replace('0b','')
    x=locationInBinary[::-1]
    while len(x)<8:
        x+='0'
    locationInBinary = x[::-1]
    return locationInBinary    


def passOne():
    global numberOfVars
    numberOfVar=0
    for line in Lines:
        if(':' in line):                                                #no ':' present in line
            error_type.error_code(-4,getLineIndex(' '.join(line)))
            exit()
        elif(line[0]=="var"):
            if(len(line)>2):                                           #more than one var defined in one line
                error_type.error_code(-4,getLineIndex(' '.join(line)))
                exit()
            elif((line[1] in Symboltable.symboltable) or Symboltable.isImm(line[1]) or (line[1] in Symboltable.registers)):
                error_type.error_code(-5,getLineIndex(' '.join(line)))      #already defined symbol used
                exit()
            else:
                numberOfVar+=1
                Symboltable.addVariable(line[1],hlt_pos+numberOfVar)   


         #[['label:','add','R0','R1','R3']]

        elif(":" in line[0]):
            label_name=line[0][0:line[0].index(":")]
            if(label_name in Symboltable.symboltable or label_name in Symboltable.registers or Symboltable.isImm(label_name) or (label_name=="var") or (label_name in op.opcode_table)):
                error_type.error_code(-4,getLineIndex(' '.join(line)))
                exit()
            else:
                 Symboltable.addLabel(label_name+":",Lines.index(line)-numberOfVar)   



def passTwo():
    program_counter=0
    for i in range(count_var,len(Lines)):           
        line_list=Lines[i];   
        if(line_list[0] not in op.opcode_table):                         #checking if label or not
            if(line_list[0] not in Symboltable.symboltable):
                error_type.error_code(-4,getLineIndex(' '.join(line_list)))
                exit()
            elif(Symboltable.symboltable[line_list[0]][0]=="variable"):
                error_type.error_code(-4,getLineIndex(' '.join(line_list)))  
                exit() 
            else:
                program_counter+=1                                       #We are on the label
                if(line_list[1] not in op.opcode_table):
                    error_type.error_code(-4,getLineIndex(' '.join(line_list)))
                    exit()
                else:
                    checkInstruction(line_list)
        else:                                                         #if first element is in opcode table 
            program_counter+=1                                         
            checkInstruction(line_list)



def checkInstruction(line_list):
    if(":" in line_list[0]):                                #creating list of only instruction
        temp_line=line_list[1:len(line_list)]
    else:
        temp_line=line_list    
    output='not set yet'   
    operation=temp_line[0]  
    dealing_key_list=op.opcode_table[operation]      
    numberOfOperands=dealing_key_list[1]
    if(operation=='mov'):
        numberOfOperands=2
    if(len(temp_line)-1!=numberOfOperands):
        print(temp_line)
        error_type.error_code(-,getLineIndex(' '.join(line_list)))
        exit()
    if(operation=='mov'):                                          #operation mov settled
        if Symboltable.isImm(temp_line[2]):
            dealing_key_list=dealing_key_list[0]
        else:
            dealing_key_list=dealing_key_list[1]
    
    if(numberOfOperands==3):                                     #type A solved i.e. with 3 registers
        for i in range(1,len(temp_line)):
            if temp_line[i] not in Symboltable.registers:
                error_type.error_code(-4,getLineIndex(' '.join(line_list)))
                exit()                      
        output=dealing_key_list[0]+"00"+Symboltable.registers[temp_line[1]]+Symboltable.registers[temp_line[2]]+Symboltable.registers[temp_line[3]]
   
    elif numberOfOperands==1:                              #type E solved i.e with the only operand mem_addr
        label=temp_line[1]+':'
        if label not in Symboltable.symboltable:
            error_type.error_code(-8,getLineIndex(' '.join(line_list))) 
            exit()  
        else:
            if Symboltable.symboltable[label][0]!='label':
                error_type.error_code(-8,getLineIndex(' '.join(line_list)))
                exit()
            else:
                output=dealing_key_list[0]+"000"+to8bitBinary(Symboltable.symboltable[label][1])
    elif numberOfOperands==0:                             #type F solved i.e. hlt statement
        output=dealing_key_list[0]+"00000000000"
    else:
        if Symboltable.isImm(temp_line[1]):
            error_type.error_code(-4,getLineIndex(' '.join(line_list)))
        else:
            if temp_line[1] in Symboltable.registers and temp_line[1]!="FLAGS":
                if Symboltable.isImm(temp_line[2]):
                    if Symboltable.inRangeImm(temp_line[2]):
                        output= dealing_key_list[0]+Symboltable.registers[temp_line[1]]+to8bitBinary(int(temp_line[2][1:len(temp_line[2])]))
                    else:
                        error_type.error_code(-9,getLineIndex(' '.join(line_list)))
                        exit()
                elif temp_line[2] in Symboltable.registers:
                    output=dealing_key_list[0]+"00000"+Symboltable.registers[temp_line[1]]+Symboltable.registers[temp_line[2]]
                elif temp_line[2] in Symboltable.symboltable:
                    if Symboltable.symboltable[temp_line[2]][0]=='label':
                        error_type.error_code(-8,getLineIndex(' '.join(line_list)))
                        exit()
                    else:
                        output= dealing_key_list[0]+Symboltable.registers[temp_line[1]]+to8bitBinary(Symboltable.symboltable[temp_line[2]][1])  
            else:
                 error_type.error_code(-9,getLineIndex(' '.join(line_list))) 
    output_list.append(output)         





def main():
    global program_counter,Lines,numberOfLines,hlt_pos,count_var,original_file_list,output_list
    # How to read and write the give test cases to inputfile.txt
    file1 = open('inputfile.txt', 'w')
    file1.truncate(0)
    for line in sys.stdin:
        file1.write(line)
    file1.close()
    file1 = open('inputfile.txt', 'r')
    Lines= file1.read().splitlines()
    file1 = open('inputfile.txt', 'r')
    original_file_list=file1.read().splitlines() 
    output_list=[]
    
    
    for i in range(0,len(original_file_list)):
        line=original_file_list[i]
        if("//" in line and line[0]!=" " and line[0]!="/"):      #Removing // after instruction in OriginalLines
            original_file_list[i]=line[0:line.index("/")].strip()
    

    for i in range(0,len(original_file_list)):
        line=original_file_list[i]
        original_file_list[i]=" ".join(line.split())


    while("" in Lines):
        Lines.remove("")                                  #removing empty lines from Lines
    for line in Lines:
        if(line[0:2]=="//"):                               #removing commented lines from Lines
            Lines.remove(line)  
    
    numberOfLines= len(Lines)          
    if(numberOfLines>256):
        error_type.error_code(-6,"")
    else:                                                                      
        for i in range(0,len(Lines)):
            line=Lines[i]
            if("//" in line):                                         #Removing // after instruction in Lines
                Lines[i]=line[0:line.index("/")].strip()
                
        
        if("hlt" in Lines[0:numberOfLines-1]  ):                      #hlt wrong position
            error_type.error_code(-1,getLineIndex("hlt"))
            exit()
        elif "hlt" not in Lines[-1]:
            error_type.error_code(-2,"")
            exit()
        else:
            hlt_pos= len(Lines)-1  


        for i in range (0,numberOfLines):                #splitting and removing extra spaces from instruction
            Lines[i]=Lines[i].split()
        
        for i in range (0,len(Lines)):
            if ("FLAGS" in Lines[i] and "mov" not in Lines[i]):
                error_type.error_code(-10,getLineIndex(' '.join(Lines[i])))
                exit()
        
        count_var=0
        for line in Lines:                                 #counting number of vars
            if (line[0]=="var"):
                count_var+=1
            else:
                break

        for i in range(0,len(Lines)):
            line=Lines[i]                                    #var in between error
            if(line[0]=="var" and i>=count_var):
                error_type.error_code(-3,getLineIndex(line))
                exit()
        hlt_pos-=count_var       
        
        
        passOne()
        passTwo()
        for lines in output_list:
            print(lines)

if __name__=="__main__":
    main()
