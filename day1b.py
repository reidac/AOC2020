
# Find two numbers in s such that v+n1+n2=2020, if they exist.
def phase2(v,s):
    s2 = s.copy()
    while(len(s2)>1):
        w = s2.pop()
        if (2020-v-w) in s2:
            return (v,w,2020-v-w)
    return None

if __name__=="__main__":
    vset = set()
    f = open("day1.txt");
    for l in f:
        vset.add(int(l))

    while(len(vset)>2):
        v = vset.pop()
        p2 = phase2(v,vset)
        if p2 is not None:
            print("Answer: ", p2[0]*p2[1]*p2[2])
            exit(0)
        
    print("Done.")
    
