import registerFiles

def add(instructions):

    reg2= instructions[10:13]
    reg3= instructions [13:16]

    temp = registerFiles.register[reg2] + registerFiles.register[reg3]
    

def sub(instructions):
    reg2= instructions[10:13]
    reg3= instructions [13:16]

    temp = registerFiles.register[reg2] - registerFiles.register[reg3]

def mul(instructions):

    reg2= instructions[10:13]
    reg3= instructions [13:16]

    temp = registerFiles.register[reg2]  * registerFiles.register[reg3]

def XOR(instructions):
    reg2= instructions[10:13]
    reg3= instructions [13:16]

    temp1 = registerFiles.register[reg2]
    temp2 = registerFiles.register[reg3]

    reg2value = integerto16bit(temp1)
    reg3value = integerto16bit(temp2)

    temp = reg2value ^ reg3value

    

def OR(instructions):

    reg2= instructions[10:13]
    reg3= instructions [13:16]

    temp1 = registerFiles.register[reg2]
    temp2 = registerFiles.register[reg3]

    reg2value = integerto16bit(temp1)
    reg3value = integerto16bit(temp2)

    temp = reg2value or reg3value

    

    

def AND(instructions):
    reg2= instructions[10:13]
    reg3= instructions [13:16]

    temp1 = registerFiles.register[reg2]
    temp2 = registerFiles.register[reg3]

    reg2value = integerto16bit(temp1)
    reg3value = integerto16bit(temp2)

    temp = reg2value and reg3value

   

def integerto16bit(value):
    value=bin(value).replace('0b','')
    x=value[::-1]
    while len(x)<16:
        x+='0'
    value = x[::-1]

    return value