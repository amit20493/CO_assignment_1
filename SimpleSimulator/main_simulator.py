import registerFiles
import executionEngine
import sys
import programCounter
import Functions
   


def to8bitBinary(location):
    locationInBinary=bin(location).replace('0b','')
    x=locationInBinary[::-1]
    while len(x)<8:
        x+='0'
    locationInBinary = x[::-1]
    return locationInBinary 


def main():
    global Lines
    halted=False
    programCounter.pc[0]=0
    '''file1 = open('binaryfile.txt', 'w')
    file1.truncate(0)
    for line in sys.stdin:
        file1.write(line)
    file1.close()'''
    file1 = open('SimpleSimulator/binaryfile.txt', 'r')
    Lines= file1.read().splitlines()
    while(len(Lines)<256):
        Lines.append("0000000000000000")
    while(not halted):
        instruction=Lines[programCounter.pc[0]]
        print(to8bitBinary(programCounter.pc[0]),end=" ")
        halted= executionEngine.execute(instruction)
        registerFiles.output()
    for line in Lines:
        print(line)

if __name__=="__main__":
    main()