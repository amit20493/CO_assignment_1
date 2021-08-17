import registerFiles
import main_simulator

def add(instruction):
    reg1= instruction[7:10]
    reg2= instruction[10:13]
    reg3= instruction [13:16]

    temp = registerFiles.register[reg2] + registerFiles.register[reg3]
    

def sub(instruction):
    reg1= instruction[7:10]
    reg2= instruction[10:13]
    reg3= instruction [13:16]

    temp = registerFiles.register[reg2] - registerFiles.register[reg3]

def mul(instruction):
    reg1= instruction[7:10]
    reg2= instruction[10:13]
    reg3= instruction [13:16]

    temp = registerFiles.register[reg2]  * registerFiles.register[reg3]

def XOR(instruction):
    reg1= instruction[7:10]
    reg2= instruction[10:13]
    reg3= instruction [13:16]

    temp1 = registerFiles.register[reg2]
    temp2 = registerFiles.register[reg3]

    reg2value = integerto16bit(temp1)
    reg3value = integerto16bit(temp2)

    temp = reg2value ^ reg3value

    

def OR(instruction):
    reg1= instruction[7:10]
    reg2= instruction[10:13]
    reg3= instruction [13:16]

    temp1 = registerFiles.register[reg2]
    temp2 = registerFiles.register[reg3]

    reg2value = integerto16bit(temp1)
    reg3value = integerto16bit(temp2)

    temp = reg2value or reg3value

    

    

def AND(instruction):
    reg1= instruction[7:10]
    reg2= instruction[10:13]
    reg3= instruction [13:16]

    temp1 = registerFiles.register[reg2]
    temp2 = registerFiles.register[reg3]

    reg2value = integerto16bit(temp1)
    reg3value = integerto16bit(temp2)

    temp = reg2value and reg3value



def load(instruction):
    reg1=instruction[6:9]
    mem_addr=binToDecimal(instruction[9:16])
    registerFiles.register[reg1]=binToDecimal(main_simulator.Lines[mem_addr])


def store(instruction):
    reg1=instruction[6:9]
    mem_addr=binToDecimal(instruction[9:16])
    main_simulator.Lines[mem_addr]=integerto16bit(registerFiles.register[reg1])
    

def jmp(instruction):
    return binToDecimal(instruction[8:16])


def jlt(instruction):
    if(registerFiles.FLAG[1]==1):
        return binToDecimal(instruction[8:16])
    return main_simulator.pc+1     


def jgt(instruction):
    if(registerFiles.FLAG[2]==1):
        return binToDecimal(instruction[8:16])
    return main_simulator.pc+1


def je(instruction):
    if(registerFiles.FLAG[3]==1):
        return binToDecimal(instruction[8:16])
    return main_simulator.pc+1

def compare(instruction):
    reg1= instruction[10:13]
    reg2= instruction[13:16]
    reg1value=registerFiles.register[reg1]
    reg2value=registerFiles.register[reg2]

    if(reg1value==reg2value):
        registerFiles.FLAG[3]=1
    
    elif(reg1value>reg2value):
        registerFiles.FLAG[2]=1
    
    elif(reg1value<reg2value):
        registerFiles.FLAG[1]=1

def integerto16bit(value):
    value=bin(value).replace('0b','')
    x=value[::-1]
    while len(x)<16:
        x+='0'
    value = x[::-1]

    return value


def binToDecimal(n):
    num = n
    value = 0
    base = 1
    temp = num
    while(temp):
        last_digit = temp % 10
        temp = int(temp / 10) 
        value+=last_digit*base
        base = base * 2
    return value
