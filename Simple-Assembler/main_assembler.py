from os import error, linesep
import OpcodeTable as op
import Symboltable
from sys import stdin




def passOne():
    for line in Lines:
        if(" " in line):
            error=-10
            break
        elif(line[0]=="var"):
            if(line[1] in Symboltable.symboltable):
                error=-16        
                

def main():
    global programme_counter,Lines,error,numberOfLines
    file1 = open('Simple-Assembler\inputfile.txt', 'r')
    #Lines = file1.readlines("\n")
    Lines= file1.read().splitlines()
    numberOfLines= len(Lines)
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
    
