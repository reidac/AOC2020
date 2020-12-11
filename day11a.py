
def update(grd):
    newgrd = {}
    for (k,v) in grd.items():
        ncount = 0
        for dlta in [(-1,0),(1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
            try:
                ncount += grd[(k[0]+dlta[0],k[1]+dlta[1])]
            except KeyError:
                pass
        if (v==0) and (ncount==0):
            newgrd[k]=1
        elif (v==1) and (ncount>=4):
            newgrd[k]=0
        else:
            newgrd[k]=v
    return newgrd

if __name__=="__main__":
    f = open("day11.txt","r")
    grid = {}
    rowct = 0
    for ln in f:
        l = ln[:-1]
        colct = 0
        for c in l:
            if c=='L':
                grid[(rowct,colct)]=0
            colct += 1
        rowct += 1

    newcount = None
    while (newcount is None) or (newcount!=oldcount):
        oldcount = newcount
        grid = update(grid)
        newcount = sum(grid.values())
        print(newcount)
        
    print("Repeated count value: %d." % newcount)
