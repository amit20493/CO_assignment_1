

#{"Name":["opcode",Number of operands,UnusedBit,StoringInRegister,UsingRegValue,ImmediateValue,MemoryAddress,CheckFlag,SetFlag]}

opcode_table={

    "add":["00000",3,2,True,True,False,False,False,False],
    "sub":["00001",3,2,True,True,False,False,False,False],
    "mov":[["00010",2,0,True,False,True,False,False,False],["00011",2,5,True,True,False,False,False,False]],
    "ld" :["00100",2,0,True,False,False,True,False,False],
    "st" :["00101",2,0,True,False,False,True,False,False],
    "mul":["00110",3,2,True,True,False,False,False,True],
    "div":["00111",2,5,True,True,False,False,False,False],
    "rs" :["01000",2,0,True,False,True,False,False,False],
    "ls" :["01001",2,0,True,False,True,False,False,False],
    "xor":["01010",3,2,True,True,False,False,False,False],
    "or" :["01011",3,2,True,True,False,False,False,False],
    "and":["01010",3,2,True,True,False,False,False,False],
    "not":["01101",2,5,True,True,False,False,False,False],
    "cmp":["01110",2,5,False,True,False,False,False,True],
    "jmp":["01111",1,3,False,False,False,True,False,False],
    "jlt":["10000",1,3,False,False,False,True,True,False],
    "jgt":["10001",1,3,False,False,False,True,True,False],
    "je" :["10000",1,3,False,False,False,True,True,False],
    "hlt":["10011",0,11,False,False,False,False,False,False]
}