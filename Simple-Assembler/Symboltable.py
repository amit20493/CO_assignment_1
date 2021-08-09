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

#decimaltobinaryconversion here tell convert the memory address of location counter to binary one
