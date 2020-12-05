import re

if __name__=="__main__":
    vmax = None
    f = open("day5.txt","r")
    for l in f:
        ll = l[:-1] # Trailing cr.
        s1 = re.sub('(B|R)','1',ll)
        s2 = re.sub('(F|L)','0',s1)
        v = int('0b'+s2,2)
        if (vmax is None) or (v>vmax):
            vmax = v
    print("Largest seat value: %d." % vmax)
