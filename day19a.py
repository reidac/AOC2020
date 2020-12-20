import re

memo = {}

# Return all the substring successors of any index.
# Memoizes.  Return value is a (possibly large) list of strings.
def substr(idx,map):
    global memo
    if idx in memo.keys():
        return memo[idx]
    else:
        v = map[idx]
        if (v[0]=='a') or (v[0]=='b'): # Terminal case.
            res = [v[0]] # Guards against some classes of weirdness.
            memo[idx] = res
            return res
        else:
            if len(v)==1: # Simple case.
                tpl = v[0]
                if len(tpl)==1:
                    res = substr(tpl[0],map)
                    memo[idx]=res
                    return res
                elif len(tpl)==2:
                    r1 = substr(tpl[0],map)
                    r2 = substr(tpl[1],map)
                    res = [ s1 + s2 for s1 in r1 for s2 in r2]
                    memo[idx]=res
                    return res
                elif len(tpl)==3:
                    r1 = substr(tpl[0],map)
                    r2 = substr(tpl[1],map)
                    r3 = substr(tpl[2],map)
                    res = [s1 + s2 + s3 for s1 in r1 for s2 in r2 for s3 in r3]
                    memo[idx]=res
                    return res
                else:
                    print("Unexpected length in simple case!")
            else: # Choice case. Tpl's are 1 or 2 only.
                res = []
                for tpl in v:
                    if len(tpl)==1:
                        contrib = substr(tpl[0],map)
                        res += contrib
                    elif len(tpl)==2:
                        r1 = substr(tpl[0],map)
                        r2 = substr(tpl[1],map)
                        contrib = [ s1 + s2 for s1 in r1 for s2 in r2]
                        res += contrib
                memo[idx] = res
                return res
            
                

if __name__=="__main__":
    f = open("day19.txt")
    fwd_map = {}
    data_set = []
    for ln in f:
        l = ln[:-1]
        if len(l)==0:
            pass
        else:
            m = re.search('([0-9]+): (.*)',l)
            if m:
                key = int(m.group(1))
                choices = m.group(2).split('|')
                vlist = []
                for cstr in choices:
                    m2 = re.findall('([0-9]+)',cstr)
                    if len(m2)!=0:
                        if len(m2)==1:
                            tpl = (int(m2[0]),)
                        elif len(m2)==2:
                            tpl = (int(m2[0]),int(m2[1]))
                        elif len(m2)==3:
                            tpl = (int(m2[0]),int(m2[1]),int(m2[2]))
                        vlist.append(tpl)
                    else:
                        vlist.append(eval(choices[0])) 
                fwd_map[key]=vlist
            m = re.search('^[ab]+$',l)
            if m:
                data_set.append(l)

    # It turns out that generating the whole freaking list is
    # not insane.   Far from optimal, but not crazy.
    megaset = set(substr(0,fwd_map))
    print(len(megaset))
    count = 0
    for d in data_set:
        if d in megaset:
            count += 1
    print("Count of valid strings from the input: %d." % count)
    

    
        
