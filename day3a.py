

if __name__=="__main__":
    f = open("day3.txt","r")
    trees = set()
    rct = 0
    for l in f:
        cct = 0
        for c in l[:-1]:  # Trailing cr.
            if c=='#':
                trees.add( (rct,cct) )
            cct += 1
        rct += 1

    # Correct for going off the end.
    print("Rows: %d, Cols: %d." % (rct,cct))

    # Go right three, down 1.
    delta = (1,3)
    pos = (0,0)
    tcount = 0
    while(pos[0]<rct):
        ppos = (pos[0],pos[1]%cct) # Periodic position.
        if (ppos in trees):
            tcount += 1
        pos = (pos[0]+delta[0],pos[1]+delta[1])

    print("Trees seen: %d" % tcount)
