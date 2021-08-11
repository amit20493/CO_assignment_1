from os import error, linesep
import OpcodeTable as op
import Symboltable
import error_type
from sys import stdin


def getLineIndex(line):
    return original_file_list.index(line)+1


def passOne():
    global numberOfVars
    numberOfVar=0
    for line in Lines:
        if("" in line or ':' in line):
            error_type.error_code(-4,getLineIndex(' '.join(line)))
            exit()
        elif(line[0]=="var"):
            if(len(line)>2):
                error_type.error_code(-4,getLineIndex(' '.join(line)))
                exit()
            elif((line[1] in Symboltable.symboltable) or Symboltable.isImm(line[1]) or (line[1] in Symboltable.registers)):
                error_type.error_code(-6,getLineIndex(' '.join(line)))
                exit()
            else:
                numberOfVar+=1
                Symboltable.addVariable(line[1],hlt_pos+numberOfVar)   
        elif(":" in line[0]):        #[['label:','add','R0','R1','R3']]
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
        if(line_list[0] not in op.opcode_table):
            if(line_list[0] not in Symboltable.symboltable):
                error_type.error_code(-4,getLineIndex(' '.join(line_list)))
            elif(Symboltable.symboltable[line_list[0]][0]=="variable"):
                error_type.error_code(-4,getLineIndex(' '.join(line_list)))   
            else:
                program_counter+=1   #We are on the label
                if(line_list[1] not in op.opcode_table):
                    print("here")
                    error_type.error_code(-4,getLineIndex(' '.join(line_list)))
                else:
                    checkInstruction(line_list)
        else:
            program_counter+=1  
            checkInstruction(line_list)


def checkInstruction(line_list):
    if(":" in line_list[0]):
        temp_line=line_list[1:len(line_list)]
    else:
        temp_line=line_list    
    operation=temp_line[0]
    if(len(temp_line)-1!=op.opcode_table[operation][1]):
        print(temp_line)
        error_type.error_code(-10,getLineIndex(' '.join(line_list)))


def main():
    global program_counter,Lines,error,numberOfLines,hlt_pos,count_var,original_file_list
    file1 = open('Simple-Assembler\inputfile.txt', 'r')
    #Lines = file1.readlines("\n")
    Lines= file1.read().splitlines()
    file1 = open('Simple-Assembler\inputfile.txt', 'r')
    original_file_list=file1.read().splitlines() 
    for line in original_file_list:
            if("//" in line and line[0]!=" " and line[0]!="/"):
                updated_line=line[0:line.index("/")].strip()
                original_file_list[original_file_list.index(line)]=updated_line 
    count_hlt=0 
    while("" in Lines):
        Lines.remove("")
    for line in Lines:
        if(line[0:2]=="//"):
            Lines.remove(line)  
    
    numberOfLines= len(Lines)          
    if(numberOfLines>255):
        error=-8
    else:
        for line in Lines:
            if("//" in line):
                updated_line=line[0:line.index("/")].strip()
                Lines[Lines.index(line)]=updated_line 

        if("hlt" in Lines[0:numberOfLines-1]  ):
            error_type.error_code(-1,getLineIndex("hlt"))
            exit()
        elif Lines[-1]!='hlt':
            error_type.error_code(-2,"")
            exit()
        else:
            hlt_pos= Lines.index('hlt')   


        for i in range (0,numberOfLines):
            Lines[i]=Lines[i].split(" ")
        count_var=0
        for line in Lines:
            if (line[0]=="var"):
                count_var+=1
            else:
                break
        for line in Lines:
            if(line[0]=="var" and Lines.index(line)>=count_var):
                error_type.error_code(-3,getLineIndex(line))
                exit()
        hlt_pos-=count_var      
        print(Lines)
        passOne()          
        print(Symboltable.symboltable)
        passTwo()

if __name__=="__main__":
    main()
    

