import re

class Ferry:
    rrgt = [[0,1],[-1,0]] # (r,c) is a left-handed coordiante system.
    rlft = [[0,-1],[1,0]] # That's why the rotation matrices look so weird.
    dirmap = {'E': (0,1), 'S': (1,0), 'W': (0,-1), 'N': (-1,0)}
    def __init__(self):
        self.pos = (0,0)
        self.waypt = (-1,10) # 10 east, one north.
    def turn(self,dirchar,amt):
        assert (amt%90==0)
        if (dirchar=='L'):
            mtx = Ferry.rlft
        elif (dirchar=='R'):
            mtx = Ferry.rrgt
        while amt != 0:
            self.waypt = (self.waypt[0]*mtx[0][0]+
                          self.waypt[1]*mtx[0][1],
                          self.waypt[0]*mtx[1][0]+
                          self.waypt[1]*mtx[1][1])
            amt -= 90
    def move(self,dirchar,amt):
        if dirchar=='F':
            self.pos = (self.pos[0]+amt*self.waypt[0],
                        self.pos[1]+amt*self.waypt[1])
        else:
            mdir = Ferry.dirmap[dirchar]
            self.waypt = (self.waypt[0]+amt*mdir[0],self.waypt[1]+amt*mdir[1])
    def __repr__(self):
        return "Ferry(%s,%s)" % (self.pos,self.waypt)
            
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
