
import re

def simple_eval(str):
    tks = str.split()
    op = None
    res = 0
    for t in tks:
        try:
            v = int(t)
        except ValueError:
            op = t
        else:
            if op is None:
                res = v
            else:
                if op=='+':
                    res += v
                elif op=='*':
                    res *= v
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
