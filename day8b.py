import sys

class CpuError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __repr__(self):
        return "CpuError: %s" % self.msg
    
class Cpu:
    def __init__(self):
        self.a = 0
        self.pc = 0
        self.instrs = []
        self.executed = set()
    def __repr__(self):
        return "Cpu(pc=%d, a=%d)" % (self.pc, self.a)
    def load(self,instrs):
        # Instrs is a list of tuples of strings.
        self.instrs = instrs
    def step(self):
        if (self.pc in self.executed):
            raise CpuError("Second hit on pc %d." % self.pc)
        else:
            self.executed.add(self.pc)
        if (len(self.instrs)==0) or (self.pc<0) or (self.pc>=len(self.instrs)):
            return False
        cur = self.instrs[self.pc]
        method = getattr(self,cur[0])
        return method(*cur[1:])
    def nop(self,*args):
        self.pc += 1
        return True
    def acc(self,*args):
        v1 = int(args[0])
        self.a += v1
        self.pc += 1
        return True
    def jmp(self,*args):
        v1 = int(args[0])
        self.pc += v1
        return True

# Test whether the CPU loops or terminates with this
# instruction set.  Because all jumps are unconditional,
# any loop is an infinite loop.

# NB does not actually really check for normal termination,
# just for an attempt to execute an out-of-bounds instruction,
# so we don't know for sure that it's tailing off the end,
# all we know is it doesn't loop.
def cpu_test(instrs):
    cpu = Cpu()
    cpu.load(instrs)
    while 1:
        try:
            res = cpu.step()
        except CpuError:
            return None
        if (not res): # Normal termination.
            return cpu.a
    
if __name__=="__main__":
    f = open("day8.txt")
    instrs = []
    for l in f:
        ops = tuple(l[:-1].split())
        instrs.append(ops)

    for idx in range(len(instrs)):
        if instrs[idx][0]=='nop':
            newinstrs = instrs[:]
            newinstrs[idx]=('jmp',instrs[idx][1])
            chk = cpu_test(newinstrs)
            if chk is not None:
                print("Normal termination, value is %d." % chk)
                break # Out of the idx loop.
        elif instrs[idx][0]=='jmp':
            newinstrs = instrs[:]
            newinstrs[idx]=('nop',instrs[idx][1])
            chk = cpu_test(newinstrs)
            if chk is not None:
                print("Normal termination, value is %d." % chk)
                break
            
                    

