import re

if __name__=="__main__":
    mem = {}
    mask = ""
    f = open("day14.txt","r")
    for ln in f:
        # Mask semantics: 0 mask bits forced to zero in result,
        #                 1 mask bits forced to one in result
        #                 X mask bits unchanged in result.
        m = re.search('mask = ([01X]+)',ln)
        if m:
            or_mask = m.group(1).replace('X','0')
            and_mask = m.group(1).replace('X','1')
            or_val = int(or_mask,2)
            and_val = int(and_mask,2)
        m = re.search('mem\[([0-9]+)\] = ([0-9]+)',ln)
        if m:
            idx = int(m.group(1))
            val = int(m.group(2))
            oval = val | or_val
            aval = oval & and_val
            mem[idx]=aval
    res = sum(mem.values())
    print("Sum: %d." % res)
              
