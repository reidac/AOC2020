
input = [15,5,1,4,7,0]
# input = [3,1,2]


if __name__=="__main__":
    lastpos = [-1]*30000000
    for i in range(len(input)-1):
        lastpos[input[i]]=(i+1) # Counts from 1.
    tailval = input[-1] # Input value not yet added to lastpos dictionary.
    pos = len(input)  # Position of the tail of the sequence.
    done = False
    #
    # For part 2, it turns out that array look-up is faster
    # than dictionary look-up, by about 20% in this case.
    while not done:
        tailpos = lastpos[tailval]
        if (tailpos==-1):
            newval = 0
        else:
            newval = pos-tailpos
        lastpos[tailval]=pos # OK to overwrite.
        tailval = newval
        if ((pos+1)==30000000):
            done = True
            print("Value at %d: %d." % (pos+1,newval))
        pos += 1
        
            
