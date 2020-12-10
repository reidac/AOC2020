
# Is v a sum of any two entries in lst?
def sumof(v,lst):
    for i in range(len(lst)):
        comp = lst[:i]+lst[i+1:]
        if (v-lst[i]) in comp:
            return True
    return False
        
if __name__=="__main__":
    f = open("day9.txt","r")
    ilst = [int(x) for x in f]
    for i in range(25,len(ilst)):
        if not sumof(ilst[i],ilst[i-25:i]):
            tval = ilst[i]
            break

    print("Target value: %d." % tval)
    # N^2 algo to start.
    bnds = None
    for i in range(len(ilst)):
        sum = ilst[i]
        for j in range(i+1,len(ilst)):
            sum += ilst[j]
            if (sum==tval):
                bnds = (i,j)
                break
        if bnds is not None:
            break

    print("Bounds for target sum: %s." % str(bnds))
    sublst = ilst[bnds[0]:bnds[1]+1]
    v1 = min(sublst)
    v2 = max(sublst)
    print("Encryption weakness: %d." % (v1+v2))
