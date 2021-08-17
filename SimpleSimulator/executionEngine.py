import registerFiles
import Functions
import main_simulator

def execute(instruction):
    
    opcode=instruction[0:5]

    if opcode == "00000":
        #add func
        Functions.add(instruction)
        main_simulator.pc+=1
        return False
        
    elif opcode == "00001":
        #sub func
        Functions.sub(instruction)
        main_simulator.pc+=1
        return False

    elif opcode == "00010":
        #movImm func
        Functions.moveImm(instruction)
        main_simulator.pc+=1
        return False
    
    elif opcode == "00011":
        #movReg func
        Functions.moveReg(instruction)
        main_simulator.pc+=1
        return False

    elif opcode == "00100":
        #store func      
        Functions.store(instruction)               
        main_simulator.pc+=1
        return False

    elif opcode == "00101":
        #load func
        Functions.load(instruction)
        main_simulator.pc+=1
        return False

    elif opcode == "00110":
        #multiply func
        Functions.mul(instruction)
        main_simulator.pc+=1
        return False       

    elif opcode == "00111":
        #divide func
        Functions.div(instruction)
        main_simulator.pc+=1
        return False

    elif opcode == "01000":
        #rightShift func
        Functions.rightShift(instruction)
        main_simulator.pc+=1
        return False

    elif opcode == "01001":
        #leftShift func
        Functions.leftShift(instruction)
        main_simulator.pc+=1
        return False

    elif opcode == "01010":
        #xor func
        Functions.XOR(instruction)
        main_simulator.pc+=1
        return False

    elif opcode == "01011":
        #or
        Functions.OR(instruction)
        main_simulator.pc+=1
        return False    

    elif opcode == "01100":
        #and
        Functions.AND(instruction)
        main_simulator.pc+=1
        return False  

    elif opcode == "01101":
        #invert
        Functions.invert(instruction)
        main_simulator.pc+=1
        return False      

    elif opcode == "01110":
        #compare
        Functions.compare(instruction)
        main_simulator.pc+=1
        return False

    elif opcode == "01111":      
        #unconditional jump                   
        main_simulator.pc=Functions.jmp(instruction)
        return False

    elif opcode == "10000":
        #less than jump
        main_simulator.pc=Functions.jlt(instruction)
        return False

    elif opcode == "10001":
        #greater than jump
        main_simulator.pc=Functions.jgt(instruction)
        return False

    elif opcode == "10010":
        #equal to jump
        main_simulator.pc=Functions.je(instruction)
        return False

    elif opcode == "10011":
        return True     