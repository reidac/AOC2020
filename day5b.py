import re

if __name__=="__main__":
    schart = [True]*1024 # There are 1024 possible values.
    f = open("day5.txt","r")
    for l in f:
        ll = l[:-1] # Trailing cr.
        s1 = re.sub('(B|R)','1',ll)
        s2 = re.sub('(F|L)','0',s1)
        v = int('0b'+s2,2)
        schart[v]=False

    # Find the "True" that's got "Falses" on both sides of it.
    for i in range(1024):
        if schart[i]:
            if not (schart[(i-1)%1024] or schart[(i+1)%1024]):
                print("Available seat: %d." % i)
