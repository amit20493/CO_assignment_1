from os import error, linesep
import OpcodeTable as op
import Symboltable
from sys import stdin




def passOne():
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
                Symboltable.addVariable(line[1],)        

def main():
    global programme_counter,Lines,error,numberOfLines,hlt_pos
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

        for lines in Lines:
            if(lines=="hlt"):
                count_hlt+=1
            if(count_hlt>1):
                print("error")
                break 
        if(Lines[-1]!="hlt"):
            print("hlt not in end of file error")  
        for i in range (0,numberOfLines):
            Lines[i]=Lines[i].split(" ")
        #passOne();    
        print(Lines)        


if __name__=="__main__":
    main()
    
