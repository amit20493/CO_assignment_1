import registerFiles
import executionEngine


def main():
    global pc, Lines
    pc=0
    halted=False
    file1 = open('SimpleSimulator/binaryfile.txt', 'r')
    Lines= file1.read().splitlines()
    while(len(Lines)<256):
        Lines.append("0000000000000000")
    while(not halted):
        instruction=Lines[pc]
        print(instruction)
        print(pc)
        halted= executionEngine.execute(instruction)
        registerFiles.print()
    for line in Lines:
        print(line)

if __name__=="__main__":
    main()