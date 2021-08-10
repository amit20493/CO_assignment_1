import OpcodeTable

symboltable={} 
'''
in symbol table i store key is variable/label ;value where at first index
store variable/label and in second index memory
allocated to variable '''

labeltable ={}

'''
label table is a dictionary where i store keys are 
labels and their value is location counter'''


def readvariables(input,location_counter):
    ''' store variables values provived '''
    if(input[location_counter][0] not in symboltable):
        print("Error"+input[location_counter][0]+"is declared but not used in assembly code")
    if(len(input[location_counter]) ==1 or len(input[location_counter][1]==0)):
        print("Error: Please provide value to variable" +str(input[location_counter][0] +""))
    validvariable(input[location_counter][1],"-" )
    symboltable[input[location_counter][0]] = [input[location_counter][1],DecimaltoBinary(location_coutner)]


    # symboltable={'y':["variable",location],'label':["label",location],}
    def addVariable(variable,location):
        pass
    def addLabel(label,location):
        pass
#decimaltobinaryconversion here tell convert the memory address of location counter to binary one
#valid variable to be declared in main file

registers={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
#DO NOT CHANGE
def isImm(imm):
    for i in imm:
        if(i=="$"):
            return True
    return False        