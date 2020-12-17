
class Cell:
    def __init__(self,alive,ncount=0):
        self.alive = alive
        self.nbcount = ncount
    def nbplus(self):
        self.nbcount += 1
    def tock(self):
        if self.alive:
            if (self.nbcount!= 2 and self.nbcount!=3):
                self.alive = False
        else:
            if (self.nbcount==3):
                self.alive = True
        self.nbcount = 0
    def __repr__(self):
        return "Cell(%s)" % self.alive

def iterate(g,d):
    # "Tick": Count up neighbors.
    # For each live cell, increment neighbor's nbcount.
    liveset = set()
    for (k,v) in g.items():
        if (v.alive):
            liveset.add(k)
    for lk in liveset:
        for dta in d:
            nb = (lk[0]+dta[0],lk[1]+dta[1],lk[2]+dta[2],lk[3]+dta[3])
            try:
                g[nb].nbplus()
            except KeyError:
                g[nb] = Cell(False,1)
    # "Tock": For all the cells, update state and clear nbcount.
    for v in g.values():
        v.tock()
    
if __name__=="__main__":
    grid = {}
    f = open("day17.txt")
    row = 0
    for ln in f:
        l = ln[:-1]
        col = 0
        for ch in l:
            if ch=="#":
                grid[(row,col,0,0)] = Cell(True)
            col += 1
        row += 1

    # print(grid)
    deltas = set()
    for r in [-1,0,1]:
        for c in [-1,0,1]:
            for z in [-1,0,1]:
                for w in [-1,0,1]:
                    delta = (r,c,z,w)
                    if delta!=(0,0,0,0):
                        deltas.add(delta)

    # print(deltas)
    for i in range(6):
        iterate(grid,deltas)

    count = 0
    for v in grid.values():
        if (v.alive):
            count += 1

    print("Live cells after 6 iterations: %d." % count)
