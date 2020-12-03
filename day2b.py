import re

if __name__=="__main__":
    vcount = 0
    f = open("day2.txt","r")
    for l in f:
        m = re.search('^([0-9]+)-([0-9]+) (.): (.*)',l)
        minct = int(m.group(1))
        maxct = int(m.group(2))
        chtr = m.group(3)
        pwd = m.group(4)

        # New schme: Exactly one of pos 1 or 2 must have the character.
        p1 = (pwd[minct-1]==chtr)
        p2 = (pwd[maxct-1]==chtr)

        if (p1 != p2):
            vcount += 1
            
    print("Valid pwds: %d." % vcount)
