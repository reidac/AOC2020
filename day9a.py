
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
            print("Found an exception: %d." % ilst[i])
            break
        
