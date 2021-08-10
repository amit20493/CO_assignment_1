from os import error, linesep
import OpcodeTable as op
import Symboltable
from sys import stdin




def passOne():
    global numberOfVars
    numberOfVar=0
    for line in Lines:
        if(" " in line):
            error=-9
            break
        elif(line[0]=="var"):
            if(len(line)>2):
                print("error")
            elif((line[1] in Symboltable.symboltable) or Symboltable.isImm(line[1]) or (line[1] in Symboltable.registers)):
                print("error")
            else:
                numberOfVar+=1
                Symboltable.addVariable(line[1],hlt_pos+numberOfVar)        

def main():
    global programme_counter,Lines,error,numberOfLines,hlt_pos,count_var
    file1 = open('Simple-Assembler\inputfile.txt', 'r')
    #Lines = file1.readlines("\n")
    Lines= file1.read().splitlines()
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

        if("hlt" in Lines[0:numberOfLines-1] or Lines[-1]!='hlt'):
            print("Error as hlt not in end")
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
                print("var in between error")   
        hlt_pos-=count_var       
        print(hlt_pos)
        passOne();  
        print(Lines)        
        print(Symboltable.symboltable)

if __name__=="__main__":
    main()
    
