import OpcodeTable as op
from sys import stdin

def main():
    global programme_counter,Lines,error
    file1 = open('inputfile.txt', 'r')
    Lines = file1.readlines()
    print(Lines)

if __name__=="__main__":
    main()
    
