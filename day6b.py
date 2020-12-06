
class Group:
    def __init__(self):
        self.ppl = 0
        self.qdata = {}
    # addq takes a string of characters.
    def addq(self,qstr):
        self.ppl += 1
        for c in qstr:
            try:
                self.qdata[c]+=1
            except KeyError:
                self.qdata[c]=1
    def total(self): # How many dictiionary entries were hit by all people?
        res = 0
        for v in self.qdata.values():
            if v==self.ppl:
                res += 1
        return res
    
if __name__=="__main__":
    total = 0 # Total of # of q's for each group.
    group = Group()
    f = open('day6.txt','r')
    for il in f:
        l = il.rstrip('\n')
        if len(l)==0:
            total += group.total()
            group = Group()
        else:
            group.addq(l)
    total += group.total() # Trailing group.
    
    print("Sum of unanimous entries over groups: %d." % total)
