def error_code(code,line):
    if code==-1:
        return print("hlt not being used as the last instruction in line"+ line )
    elif code==-2:
        return print("Missing hlt instruction in line"+ line)
    elif code==-3:
        return print("Variables not declared at the beginning in line"+ line)
    elif code==-4:
        return print("Syntax error in line "+ str(line))     #doubt
    elif code==-5:
        return print("Wrong syntax used in line "+  str(line)) #IMP
    elif code==-6:
        return print("Wrong var type provided in line"+ line) 
    elif code==-7:
        print("Opcode cannot be used as a variable in line"+ line)
    elif code==-8:
        print("Cannot fit program in given space (bigger than 255 lines) in line"+ line)     
    elif code==-9:
        print("Syntax Error")
    elif code==-10:
        print("Extra operand provided "+str(line))
    elif code==-11:
        print("Needs more operands") 
    elif code==-12:
        print("Not defined in above program")
    elif code==-13:
        print("called in middle of program(not allowed) ")     
    elif code==-14:
        print("Not found"+str)
    elif code==-15:
        print("Lable not initialised")
    elif code==-16:
        print("Variable is previsously intialised")  