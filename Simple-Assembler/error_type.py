def error_code(code,line):
    if code==-1:
        return ("hlt not being used as the last instruction in line "+ str(line)+" or multiple hlt being used " )
    elif code==-2:
        return ("Missing hlt instruction")
    elif code==-3:
        return ("Variables not declared at the beginning in line"+ str(line))
    elif code==-4:
        return ("Syntax error in line "+ str(line))     #doubt
    elif code==-5:
        return ("Wrong var type provided in line "+ str(line))  #IMP
    elif code==-6:
        return ("Cannot fit program in given space (bigger than 255 lines) in line "+ str(line)) 
    elif code==-7:
        return ("Extra operand provided in line "+str(line))
    elif code==-8:
       return ("Lable not initialised in line "+ str(line))     
    elif code==-9:
        return ("Illegal Immediate values (less than 0 or more than 255) in line "+ str(line))
    elif code==-10:
       return ("Illegal use of FLAGS in line "+str(line))
    elif code==-11:
        return ("Invalid number of operands"+str(line))   
           