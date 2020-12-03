

if __name__=="__main__":
    vset = set()
    f = open("day1.txt");
    for l in f:
        vset.add(int(l))

    while(len(vset)>2):
        v = vset.pop()
        if (2020-v) in vset:
            print("Found complment for ",v)
            print("Actual answer: ",v*(2020-v))
    print("Done.")
    
