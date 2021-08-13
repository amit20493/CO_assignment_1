from sys import flags
import OpcodeTable
import main
import error_type

symboltable={} 
'''
in symbol table i store key is variable/label ;value where at first index
store variable/label and in second index memory
allocated to variable and 
labels and their value is location counter'''

# symboltable={'y':["variable",location],'label':["label",location],}
def addVariable(variable,location):
    symboltable[variable]=["variable",location]
def addLabel(label,location):
    symboltable[label]=["label",location]


    
#valid variable to be declared in main file
#validlabel to be declared in main file

registers = {"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
#DO NOT CHANGE
def isImm(imm):  
    for i in imm:
        if(i=="$"):
            return True
    return False   

def inRangeImm(imm):
    return (int(imm[1:len(imm)])>=0 and int(imm[1:len(imm)])<256)  

