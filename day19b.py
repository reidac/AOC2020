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

    # Part 2.
    # Rule changes.
    # fwd_map[8] = [(42,),(42,8)] // was [(42,)]
    # fwd_map[11] = [(42,31),(42,11,31)]  // was [(42,31)]
    # The effect of these is to allow arbitrary numbers
    # of nested (42,31) pairs (like: 42,42,42,31,31,31)
    # or 42's in a row.
    #
    # Top-level rule is fwd_map[0] = [(8,11)], so in the
    # old scheme, rule-42 and (rule 42, rule 31) were "atoms".
    #
    # The longest candidate entry is 96 characters.
    # Rule 31 and 42 outputs are 8 places, and we must have at least
    # 3 of them in the most basic case (using up 24 places).
    # Redundant applcation of rule 8 adds 8 places.
    # Redundant application of rule 11 adds 16.
    # so at most 9 extra applications of rule 8, and at most
    # 4 extra rule 11's, and they interact.

    # For a given string, iterate over the possible structures,
    # is the scheme, using rule-42 and rule-31 lists as "basis sets",
    # with the structure being some number of rule-42 compliant
    # octets, followed by nested 42-31 pairs.
    sub42 = set(substr(42,fwd_map))
    sub31 = set(substr(31,fwd_map))
    
    # So the real question is, which of the previously-rejected strings
    # have the property that they contain one of these patterns,
    # and in the absence of this pattern, would have been accepted?
    # How to find contiguous non-overlapping repeated substrings?
    count = 0
    for d in data_set:
        if len(d)==24:
            if ((d[0:8] in sub42) and (d[8:16] in sub42) and
                (d[16:24] in sub31)):
                count += 1
        
    print("Test count: %d." % count)

    count = 0
    for d in data_set:
        maxprefix = int((len(d)-16)/8) # Include base case.
        valid = False
        for pcount in range(1,maxprefix+1):
            pvalid = True
            if (((len(d)-pcount*8)/8)%2)!=0:
                pvalid = False
            else:
                icount = int((len(d)-pcount*8)/16)
                for i in range(pcount+icount):
                    if (d[i*8:(i+1)*8] not in sub42):
                        pvalid = False
                for i in range(pcount+icount,pcount+2*icount):
                    if (d[i*8:(i+1)*8] not in sub31):
                        pvalid = False
            if (pvalid): # If any p-state is valid, the datum is valid.
                valid = True
        if (valid):
            count += 1

    print("Final valid count: %d." % count)
            
        
