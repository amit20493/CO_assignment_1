register={"000":0,"001":0,"010":1990,"011":11,"100":0,"101":0,"110":0,"111":0}

#def to16bitBinary(location):

for  key,value in register.items():
    value=bin(value).replace('0b','')
    x=value[::-1]
    while len(x)<16:
        x+='0'
    value = x[::-1]
    print(value , end=" ")

#print function to print spcae separated 16 bit value of register
#make func to convert into 