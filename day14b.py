import re

# Iterate over all substitutions for X's.
def xpand(str):
    xdx = str.find('X')
    if (xdx<0):
        yield str
    else:
        zerpfx = str[:xdx]+'0'
        onepfx = str[:xdx]+'1'
        for tl in xpand(str[xdx+1:]):
            yield zerpfx+tl
            yield onepfx+tl

    
if __name__=="__main__":
    mem = {}
    base = ""
    f = open("day14.txt","r")
    for ln in f:
        # Mask semantics: 0 mask bits forced to zero in result,
        #                 1 mask bits forced to one in result
        #                 X mask bits unchanged in result.
        m = re.search('mask = ([01X]+)',ln)
        if m:
            base = m.group(1).replace('0','z')
        m = re.search('mem\[([0-9]+)\] = ([0-9]+)',ln)
        if m:
            addr = int(m.group(1))
            val = int(m.group(2))
            for mask in xpand(base):
                # Mask semantics as above, but on the address for pt.2.
                or_mask = mask.replace('z','0')
                and_mask = mask.replace('z','1')
                oaddr = addr | int(or_mask,2)
                aaddr = oaddr & int(and_mask,2)
                mem[aaddr] = val
    res = sum(mem.values())
    print("Sum: %d." % res)
              
