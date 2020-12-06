
if __name__=="__main__":
    total = 0 # Total of # of q's for each group.
    group = set()
    f = open('day6.txt','r')
    for il in f:
        l = il.rstrip('\n')
        if len(l)==0:
            inc = len(group)
            total += inc
            group=set()
        else:
            for c in l:
                group.add(c)
    inc = len(group)
    total += inc # Trailing group.
    
    print("Sum of unique entries over groups: %d." % total)
