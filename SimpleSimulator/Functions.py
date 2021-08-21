import registerFiles
import programCounter
import Memory

def add(instruction):
    for i in range(4):
        registerFiles.FLAG[i]="0"
    reg1= instruction[7:10]
    reg2= instruction[10:13]
    reg3= instruction [13:16]

    temp = registerFiles.register[reg2] + registerFiles.register[reg3]
    if temp >= (2**16):
        registerFiles.FLAG[0]="1"
        temp=temp%(2**16)
    registerFiles.register[reg1]=temp


    
    

def sub(instruction):
    for i in range(4):
        registerFiles.FLAG[i]="0"
    reg1= instruction[7:10]
    reg2= instruction[10:13]
    reg3= instruction [13:16]

    temp = registerFiles.register[reg2] - registerFiles.register[reg3]

    if temp <0:
        registerFiles.FLAG[0]="1"
        temp=0
    registerFiles.register[reg1]=temp
          

def mul(instruction):
    for i in range(4):
        registerFiles.FLAG[i]="0"
    reg1= instruction[7:10]
    reg2= instruction[10:13]
    reg3= instruction [13:16]

    temp = registerFiles.register[reg2]  * registerFiles.register[reg3]
    if temp >= (2**16):
        registerFiles.FLAG[0]="1"
        temp=temp%(2**16)
    registerFiles.register[reg1]=temp



def div(instruction):
    reg3= instruction[10:13]
    reg4= instruction[13:16]
    registerFiles.register["000"]=reg3/reg4
    registerFiles.register["001"]=reg3%reg4
    for i in range(4):
        registerFiles.FLAG[i]="0"


def moveReg(instruction):
    reg1= instruction[10:13]
    reg2= instruction[13:16]
    if(reg2=="111"):
        temp="000000000000"+"".join(registerFiles.FLAG)
        tempo=binToDecimal(temp)
    else:
        tempo=registerFiles.register[reg2]    
    registerFiles.register[reg1]=tempo
    for i in range(4):
        registerFiles.FLAG[i]="0"


def moveImm(instruction):
    reg1=instruction[5:8]
    registerFiles.register[reg1]=binToDecimal(instruction[8:16])
    for i in range(4):
        registerFiles.FLAG[i]="0"






def XOR(instruction):
    reg1= instruction[7:10]
    reg2= instruction[10:13]
    reg3= instruction [13:16]

    temp1 = registerFiles.register[reg2]
    temp2 = registerFiles.register[reg3]

    temp = temp1 ^ temp2
    registerFiles.register[reg1]=temp
    for i in range(4):
        registerFiles.FLAG[i]="0"
    

def OR(instruction):
    reg1= instruction[7:10]
    reg2= instruction[10:13]
    reg3= instruction [13:16]

    temp1 = registerFiles.register[reg2]
    temp2 = registerFiles.register[reg3]

    temp = temp1 or temp2
    registerFiles.register[reg1]=temp
    for i in range(4):
        registerFiles.FLAG[i]="0"

    

    

def AND(instruction):
    reg1= instruction[7:10]
    reg2= instruction[10:13]
    reg3= instruction [13:16]

    temp1 = registerFiles.register[reg2]
    temp2 = registerFiles.register[reg3]

    temp = temp1 and temp2
    registerFiles.register[reg1]=temp
    for i in range(4):
        registerFiles.FLAG[i]="0"





def invert(instruction):
    reg1= instruction[10:13]
    reg2= instruction[13:16]
    registerFiles.register[reg1]=(2**16)-registerFiles.register[reg2]-1
    for i in range(4):
        registerFiles.FLAG[i]="0"


def load(instruction):
    reg1=instruction[5:8]
    mem_addr=binToDecimal(instruction[8:16])
    registerFiles.register[reg1]=binToDecimal(Memory.Lines[mem_addr])
    for i in range(4):
        registerFiles.FLAG[i]="0"
    return mem_addr


def store(instruction):
    reg1=instruction[5:8]
    mem_addr=binToDecimal(instruction[8:16])
    Memory.Lines[mem_addr]=integerto16bit(registerFiles.register[reg1])
    for i in range(4):
        registerFiles.FLAG[i]="0"
    return mem_addr    
    

def jmp(instruction):
    for i in range(4):
        registerFiles.FLAG[i]="0"
    return binToDecimal(instruction[8:16])
    


def jlt(instruction):
    if(registerFiles.FLAG[1]=="1"):
        for i in range(4):
                registerFiles.FLAG[i]="0"
        return binToDecimal(instruction[8:16])
    for i in range(4):
        registerFiles.FLAG[i]="0"    
    return programCounter.pc[0]+1     


def jgt(instruction):
    if(registerFiles.FLAG[2]=="1"):
        for i in range(4):
            registerFiles.FLAG[i]="0"
        return binToDecimal(instruction[8:16])
    for i in range(4):
        registerFiles.FLAG[i]="0"
    return programCounter.pc[0]+1


def je(instruction):
    if(registerFiles.FLAG[3]=="1"):
        for i in range(4):
            registerFiles.FLAG[i]="0"
        return binToDecimal(instruction[8:16])
    for i in range(4):
        registerFiles.FLAG[i]="0"
    return programCounter.pc[0]+1


def compare(instruction):
    for i in range(4):
        registerFiles.FLAG[i]="0"
    reg1= instruction[10:13]
    reg2= instruction[13:16]
    reg1value=registerFiles.register[reg1]
    reg2value=registerFiles.register[reg2]

    if(reg1value==reg2value):
        registerFiles.FLAG[3]="1"
    
    elif(reg1value>reg2value):
        registerFiles.FLAG[2]="1"
    
    elif(reg1value<reg2value):
        registerFiles.FLAG[1]="1"



def rightShift(instruction):
    reg1=instruction[5:8]
    imm= binToDecimal(instruction[8:16])
    registerFiles.register[reg1]=(registerFiles.register[reg1])/(2**imm)
    for i in range(4):
        registerFiles.FLAG[i]="0"
    

def leftShift(instruction):
    reg1=instruction[5:8]
    imm= binToDecimal(instruction[8:16])
    registerFiles.register[reg1]=(registerFiles.register[reg1])*(2**imm)
    for i in range(4):
        registerFiles.FLAG[i]="0"



def integerto16bit(value):
    value=bin(value).replace('0b','')
    x=value[::-1]
    while len(x)<16:
        x+='0'
    value = x[::-1]

    return value


def binToDecimal(n):
    return int(n,2)
