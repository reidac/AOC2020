
def update(grd):
    # First update neighbor counts.
    for v in grd.values():
        if v.occupied==1:
            for p in v.nbrs:
                grd[p].nbcount += 1

    for v in grd.values():
        if (v.occupied==0) and (v.nbcount==0):
            v.occupied = 1
        elif (v.occupied==1) and (v.nbcount >= 5):
            v.occupied = 0
        # Otherwise v.occupied is unchanged.
        v.nbcount = 0 # Reset for next iteration.
            

# Chairs don't really need to know their position.
class Chair:
    def __init__(self,pos):
        self.pos = pos
        self.nbrs = set() # of coordinates.
        self.occupied = 0
        self.nbcount = 0
    def __repr__(self):
        return "Chair(%d,%d):%d" % (self.pos[0],self.pos[1],self.occupied)

if __name__=="__main__":
    f = open("day11.txt","r")
    grid = {}
    rowct = 0
    for ln in f:
        l = ln[:-1]
        colct = 0
        for c in l:
            if c=='L':
                grid[(rowct,colct)]=Chair( (rowct,colct) )
            colct += 1
        rowct += 1
        
    # Everybody find their neighbors.
    for k in grid.keys():
        for dlta in [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]:
            r=1
            done = False
            while not done:
                npos = (k[0]+r*dlta[0],k[1]+r*dlta[1])
                if ((npos[0]<0) or (npos[0]>rowct) or
                    (npos[1]<0) or (npos[1]>colct)):
                    done = True
                try:
                    c = grid[npos]
                except KeyError:
                    pass
                else:
                    grid[k].nbrs.add(npos)
                    done = True
                r+=1

    # At this point, every chair knows all its neighobrs.
    
    newcount = None
    while (newcount is None) or (newcount!=oldcount):
        oldcount = newcount
        update(grid)
        newcount = sum( [c.occupied for c in grid.values() ] )
        print(newcount)

    print("Repeated count value: %d." % newcount)
