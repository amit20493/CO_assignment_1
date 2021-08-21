import registerFiles
import executionEngine
import sys
import programCounter
import Memory
   


def to8bitBinary(location):
    locationInBinary=bin(location).replace('0b','')
    x=locationInBinary[::-1]
    while len(x)<8:
        x+='0'
    locationInBinary = x[::-1]
    return locationInBinary 


def main():
    global plot_list
    plot_list=[]
    cycle=0
    halted=False
    programCounter.pc[0]=0
    file1 = open('binaryfile.txt', 'w')
    file1.truncate(0)
    for line in sys.stdin:
        file1.write(line)
    file1.close()
    file1 = open('binaryfile.txt', 'r')
    Memory.Lines= file1.read().splitlines()
    while(len(Memory.Lines)<256):
        Memory.Lines.append("0000000000000000")
    while(not halted):
        instruction=Memory.Lines[programCounter.pc[0]]
        plot_list.append([cycle,programCounter.pc[0]])
        print(to8bitBinary(programCounter.pc[0]),end=" ")
        halted= executionEngine.execute(instruction,cycle)
        registerFiles.output()
        cycle+=1
    for line in Memory.Lines:
        print(line)
    x_axis,y_axis=zip(*plot_list)
    plt.plot(x_axis,y_axis)
    plt.savefig('plot.png')


if __name__=="__main__":
    main()