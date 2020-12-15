
input = [15,5,1,4,7,0]
# input = [3,1,2]


if __name__=="__main__":
    lastpos = {}
    for i in range(len(input)-1):
        lastpos[input[i]]=(i+1) # Counts from 1.
    tailval = input[-1] # Input value not yet added to lastpos dictionary.
    pos = len(input)  # Position of the tail of the sequence.
    done = False
    #
    # For part 2, the "naive" algorithm gets to 30 million
    # in 1 m 10s on the Rpi4.  Sufficient, but probably
    # not optimal.
    while not done:
        try:
            tailpos = lastpos[tailval]
        except KeyError:
            newval = 0
        else:
            newval = pos-tailpos
        lastpos[tailval]=pos # OK to overwrite.
        tailval = newval
        if ((pos+1)==30000000):
            done = True
            print("Value at %d: %d." % (pos+1,newval))
        pos += 1
        if (pos%100000)==0: # Reassurance.
            print(pos)
        
            
