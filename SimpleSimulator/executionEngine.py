import Functions
import main_simulator
import programCounter
import registerFiles


def execute(instruction,cycle):
    
    opcode=instruction[0:5]

    if opcode == "00000":
        #add func
        Functions.add(instruction)
        programCounter.pc[0]+=1
        return False
        
    elif opcode == "00001":
        #sub func
        Functions.sub(instruction)
        programCounter.pc[0]+=1
        return False

    elif opcode == "00010":
        #movImm func
        Functions.moveImm(instruction)
        programCounter.pc[0]+=1
        return False
    
    elif opcode == "00011":
        #movReg func
        Functions.moveReg(instruction)
        programCounter.pc[0]+=1
        return False

    elif opcode == "00101":
        #store func      
        mem_addr=Functions.store(instruction)
        main_simulator.Memory.plot_list.append([cycle,mem_addr])               
        programCounter.pc[0]+=1
        return False

    elif opcode == "00100":
        #load func
        mem_addr=Functions.load(instruction)
        main_simulator.Memory.plot_list.append([cycle,mem_addr])
        programCounter.pc[0]+=1
        return False

    elif opcode == "00110":
        #multiply func
        Functions.mul(instruction)
        programCounter.pc[0]+=1
        return False       

    elif opcode == "00111":
        #divide func
        Functions.div(instruction)
        programCounter.pc[0]+=1
        return False

    elif opcode == "01000":
        #rightShift func
        Functions.rightShift(instruction)
        programCounter.pc[0]+=1
        return False

    elif opcode == "01001":
        #leftShift func
        Functions.leftShift(instruction)
        programCounter.pc[0]+=1
        return False

    elif opcode == "01010":
        #xor func
        Functions.XOR(instruction)
        programCounter.pc[0]+=1
        return False

    elif opcode == "01011":
        #or
        Functions.OR(instruction)
        programCounter.pc[0]+=1
        return False    

    elif opcode == "01100":
        #and
        Functions.AND(instruction)
        programCounter.pc[0]+=1
        return False  

    elif opcode == "01101":
        #invert
        Functions.invert(instruction)
        programCounter.pc[0]+=1
        return False      

    elif opcode == "01110":
        #compare
        Functions.compare(instruction)
        programCounter.pc[0]+=1
        return False

    elif opcode == "01111":      
        #unconditional jump                   
        programCounter.pc[0]=Functions.jmp(instruction)
        return False

    elif opcode == "10000":
        #less than jump
        programCounter.pc[0]=Functions.jlt(instruction)
        return False

    elif opcode == "10001":
        #greater than jump
        programCounter.pc[0]=Functions.jgt(instruction)
        return False

    elif opcode == "10010":
        #equal to jump
        programCounter.pc[0]=Functions.je(instruction)
        return False

    elif opcode == "10011":
        for i in range(4):
            registerFiles.FLAG[i]="0"
        return True     