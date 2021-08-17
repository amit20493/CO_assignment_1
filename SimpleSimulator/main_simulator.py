import registerFiles
import executionEngine


def main():
    global pc
    pc=0
    halted=False
    file1 = open('SimpleSimulator/binaryfile.txt', 'r')
    Lines= file1.read().splitlines()
    while(not halted):
        instruction=Lines[pc]
        print(instruction)
        halted= executionEngine.execute(instruction)
        print(pc)
        registerFiles.print()
    for line in Lines:
        print(line)

if __name__=="__main__":
    main()