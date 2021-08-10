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
    global programme_counter,Lines,error,numberOfLines,halt_pos
    file1 = open('Simple-Assembler\inputfile.txt', 'r')
    #Lines = file1.readlines("\n")
    Lines= file1.read().splitlines()

    numberOfLines= len(Lines)
    count_hlt=0
    while("hlt" in Lines):
        count_hlt+=1
    if(count_hlt>1):
        print("")    
    while("" in Lines):
        Lines.remove("")
        numberOfLines-=1
    if(numberOfLines>255):
        error=-8
    else:
        for i in range (0,numberOfLines):
            Lines[i]=Lines[i].split(" ")
        passOne();    
                    
    print(Lines)
if __name__=="__main__":
    main()
    
