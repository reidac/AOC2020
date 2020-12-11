

def sublist(n,lst):
    if n==len(lst):
        yield lst
    elif n==1:
        for l in lst:
            yield [l]
    else:
        for t in sublist(n-1,lst[1:]):
            yield [lst[0]]+t
        for t in sublist(n,lst[1:]):
            yield t
        

def subsets(lst):
    for i in range(1,len(lst)):
        for s in sublist(i,lst):
            yield s
            
# Count valid configurations of a sub-list, lst, that
# has to link vstart and vend within 3.
def valid_count(vstart,vend,lst):
    vcount = 0
    for s in subsets(lst):
        if len(s)==0:
            break
        if len(s)==1:
            if (s[0]-vstart<=3) and (vend-s[0]<=3):
                vcount += 1
        else:
            if(s[0]-vstart>3):
                break
            if (vend-s[-1]>3):
                break
            for i in range(len(s)-1):
                if (s[i+1]-s[i]>3):
                    break
            else:
                vcount += 1
    # End check. Might be OK to remove all of them?
    if (vend-vstart)<=3:
        vcount += 1
    return vcount
            
if __name__=="__main__":
    f = open("day10.txt","r")
    ilst = [int(x) for x in f]
    ilst.sort()

    # Test case #1, 8 configs.
    # ilst = [1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19]

    # Test case #2, 19208 configs.
    # ilst = [1,2,3,4,7,8,9,10,11,14,17,18,19,20,23,24,25,28,31,32,33,34,35,38,39,42,45,46,47,48,49]


    l2 = [0]*len(ilst)
    # 1st element manually:
    if ilst[1]>=3:
        l2[0]=0
    else:
        l2[0] = 1 
    for i in range(1,len(ilst)-1):
        if ((ilst[i+1]-ilst[i-1])<=3):
            l2[i]=1
    i = 0
    ccount = 1
    done = False
    while not done:
        # Find contiguous subgroups.
        if l2[i]==1:
            j=0
            while l2[i+j]==1:
                j+=1
            if j==1:
                ccount *= 2
            else:
                if (i==0):
                    vmin = 0
                else:
                    vmin = ilst[i-1]
                vmax = ilst[i+j]
                sublst = ilst[i:i+j]
                vct = valid_count(vmin,vmax,sublst)
                ccount *= (vct+1) # Subsets leave out trivial case.
            i=i+j
        else:
            i+=1
            if i==len(ilst):
                done = True

    print("Valid config count: %d." % ccount)
                
