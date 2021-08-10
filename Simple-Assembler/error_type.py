def error_code(code):
    if code==-1:
        print("Opcode not founnd")
    elif code==-2:
        print("Symbol not found in Symbol Table")
    elif code==-3:
        print("Symbol defined as varaiable cannot be used as a label")
    elif code==-4:
        print("Label is previsously intialised")     
    elif code==-5:
        print("Cannot use label as a variable")
    elif code==-6:
        print("Opcode cannot be used as a label") 
    elif code==-7:
        print("Opcode cannot be used as a variable")
    elif code==-8:
        print("Cannot fit program in given space (bigger than 255 lines)")     
    elif code==-9:
        print("Syntax Error")
    elif code==-10:
        print("Extra operand provided")
    elif code==-11:
        print("Needs more operands") 
    elif code==-12:
        print("Not defined in above program")
    elif code==-13:
        print("called in middle of program(not allowed) ")     
    elif code==-14:
        print("Not found")
    elif code==-15:
        print("Lable not initialised")
    elif code==-16:
        print("Variable is previsously intialised")  