import re

class Ferry:
    lftmap = {(0,1):(-1,0), (-1,0):(0,-1), (0,-1):(1,0), (1,0):(0,1)}
    rgtmap = {(0,1):(1,0), (1,0):(0,-1), (0,-1):(-1,0), (-1,0):(0,1)}
    dirmap = {'E': (0,1), 'S': (1,0), 'W': (0,-1), 'N': (-1,0)}
    def __init__(self):
        self.pos = (0,0)
        self.dir = (0,1) # East.
    def turn(self,dirchar,amt):
        assert (amt%90==0)
        if (dirchar=='L'):
            map = Ferry.lftmap
        elif (dirchar=='R'):
            map = Ferry.rgtmap
        while amt != 0:
            self.dir = map[self.dir]
            amt -= 90
    def move(self,dirchar,amt):
        if dirchar=='F':
            self.pos = (self.pos[0]+amt*self.dir[0],self.pos[1]+amt*self.dir[1])
        else:
            mdir = Ferry.dirmap[dirchar]
            self.pos = (self.pos[0]+amt*mdir[0],self.pos[1]+amt*mdir[1])
    def __repr__(self):
        return "Ferry(%s,%s)" % (self.pos,self.dir)
            
if __name__=="__main__":
    fr = Ferry()
    f = open("day12.txt")
    for ln in f:
        l = ln[:-1]
        print("Command: %s." % l)
        m = re.match('^(N|S|E|W|F){1}([0-9]+)',l)
        if m:
            mvdir = m.group(1)
            mvamt = int(m.group(2))
            fr.move(mvdir,mvamt)
        m = re.match('^(L|R){1}([0-9]+)',l)
        if m:
            tndir = m.group(1)
            tnamt = int(m.group(2))
            fr.turn(tndir,tnamt)
            
    print(fr)
    print("Manhattan distance: %d." % (abs(fr.pos[0])+abs(fr.pos[1])))
