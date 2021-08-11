def error_code(code):
    if code==-1:
        return print("hlt not being used as the last instruction")
    elif code==-2:
        return print("Missing hlt instruction")
    elif code==-3:
        return print("Variables not declared at the beginning")
    elif code==-4:
        return print("Syntax error")     #doubt
    elif code==-5:
        return print("Wrong syntax used") #IMP
    elif code==-6:
        return print("Wrong var type provided") 
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