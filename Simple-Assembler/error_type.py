def error_code(code,line):
    if code==-1:
        return print("hlt not being used as the last instruction in line "+ str(line) )
    elif code==-2:
        return print("Missing hlt instruction")
    elif code==-3:
        return print("Variables not declared at the beginning in line"+ str(line))
    elif code==-4:
        return print("Syntax error in line "+ str(line))     #doubt
    elif code==-5:
        return print("Wrong syntax used in line "+  str(line)) #IMP
    elif code==-6:
        return print("Wrong var type provided in line "+ str(line)) 
    elif code==-7:
        print("Opcode cannot be used as a variable in line "+ str(line))
    elif code==-8:
        print("Cannot fit program in given space (bigger than 255 lines) in line "+ str(line))     
    elif code==-9:
        print("Syntax Error in line "+str(line))
    elif code==-10:
        print("Extra operand provided "+str(line))
    elif code==-11:
        print("Needs more operands "+str(line)) 
    elif code==-12:
        print("Not defined in above program "+str(line))
    elif code==-13:
        print("called in middle of program(not allowed) "+str(line))     
    elif code==-14:
        print("Not found "+ str(line))
    elif code==-15:
        print("Lable not initialised "+ str(line))
    elif code==-16:
        print("Variable is previsously intialised " +str(line))  
    elif code==-17:
        print("Illegal Immediate values (less than 0 or more than 255) in line "+ str(line))
    elif code==-18:
        print("Illegal use of FLAGS in line "+str(line))       