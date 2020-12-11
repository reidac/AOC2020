
        
if __name__=="__main__":
    f = open("day10.txt","r")
    ilst = [int(x) for x in f]
    ilst.sort()

    print(ilst)
    
    threecount = 1 # The terminal device counts here.
    onecount = 1
    for i in range(len(ilst)-1):
        delt = ilst[i+1]-ilst[i]
        if delt==3:
            threecount += 1
        elif delt==1:
            onecount += 1


    print("Jolt difference product: %d." % (onecount*threecount) )
        
