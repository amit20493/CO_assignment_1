import Memory
import programCounter
import registerFiles
import executionEngine


def main():
    memory=Memory()
    rf=registerFiles()
    PC=programCounter(0)
    halted=False

    while(not halted):
        inst=memory.getInst(PC.getVal())
        halted, new_PC= executionEngine.execute(inst)
        PC.dump()
        rf.dump()
        PC.update(new_PC)
    memory.dump()    
