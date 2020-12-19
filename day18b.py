
import re

def simple_eval(stng):
    tks = stng.split()
    # Addition pass.
    done = False
    while not done:
        try:
            idx = tks.index('+')
        except ValueError:
            done = True
        else:
            sum = int(tks[idx-1])+int(tks[idx+1])
            nlst = tks[:idx-1] + [str(sum)] + tks[idx+2:]
            tks = nlst
    # Multiplication pass.
    res = int(tks[0])
    for idx in range(2,len(tks),2):
        res *= int(tks[idx])
    return res
        
    

def ceval(stng):
    done = False
    while not done:
        # Find matching parenthesis pairs.
        m = re.search('(\([ 0-9+*]+\))',stng)
        if m is None:
            done = True
        else:
            mstr = m.group()
            newhd = stng[:m.span()[0]]
            newtl = stng[m.span()[1]:]
            newmid = str(simple_eval(mstr[1:-1]))
            stng = newhd+newmid+newtl
    return simple_eval(stng)
                                     
        
if __name__=="__main__":
    # v1 = ceval('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')
    # print(v1)
    res = 0
    f = open("day18.txt")
    for ln in f:
        res += ceval(ln[:-1])
    print("Sum of evalutions: %d." % res)
