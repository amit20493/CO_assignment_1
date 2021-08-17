import registerFiles
import main_simulator

def execute(instruction):
    
    opcode=instruction[0:5]

    if opcode == "00000":
        #add func
        main_simulator.pc+=1
        return False
        
    elif opcode == "00001":
        #sub func
        main_simulator.pc+=1
        return False

    elif opcode == "00010":
        #movImm func
        main_simulator.pc+=1
        return False
    
    elif opcode == "00011":
        #movReg func
        main_simulator.pc+=1
        return False

    elif opcode == "00100":
        #store func                     
        main_simulator.pc+=1
        return False

    elif opcode == "00101":
        #load func
        main_simulator.pc+=1
        return False

    elif opcode == "00110":
        #multiply func
        main_simulator.pc+=1
        return False       

    elif opcode == "00111":
        #divide func
        main_simulator.pc+=1
        return False

    elif opcode == "01000":
        #rightShift func
        main_simulator.pc+=1
        return False

    elif opcode == "01001":
        #leftShift func
        main_simulator.pc+=1
        return False

    elif opcode == "01010":
        #xor func
        main_simulator.pc+=1
        return False

    elif opcode == "01011":
        #or
        main_simulator.pc+=1
        return False    

    elif opcode == "01100":
        #and
        main_simulator.pc+=1
        return False  

    elif opcode == "01101":
        #invert
        main_simulator.pc+=1
        return False      

    elif opcode == "01110":
        #compare
        main_simulator.pc+=1
        return False

    elif opcode == "01111":                         
        #main_simulator.pc=jump(instruction)
        return False

    elif opcode == "10000":
        #main_simulator.pc=jlt(instruction)
        return False

    elif opcode == "10001":
        #main_simulator.pc=jgt(instruction)
        return False

    elif opcode == "10010":
        #main_simulator.pc=jump(instruction)
        return False

    elif opcode == "10011":
        return True     