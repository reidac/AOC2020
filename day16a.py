import re

if __name__=="__main__":
    f = open("day16.txt")
    nearby_seen = False
    range_dict = {}
    error_rate = 0
    for ln in f:
        m = re.search('^(.*): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)',ln)
        if m:
            datum = m.group(1)
            range1 = (int(m.group(2)),int(m.group(3)))
            range2 = (int(m.group(4)),int(m.group(5)))
            range_dict[datum] = [range1,range2]

        # All ranges are specified before any tickets are seen.
        # print(range_dict)
        
        m = re.search('^nearby tickets:',ln)
        if m:
            nearby_seen = True

        m = re.search('^(([0-9]+),)+[0-9]+',ln)
        if m:
            if not nearby_seen:
                pass # This is our ticket.  For part 1, ignore it.
            else:
                vals = map(int,re.findall('[0-9]+',ln))
                # Check validity.
                for v in vals:
                    valid = False # "valid" means fits in at least one range.
                    for rl in range_dict.values():
                        for rng in rl:
                            if (v>=rng[0]) and (v<=rng[1]):
                                valid = True
                                break
                        if valid:
                            break
                    if not valid:
                        error_rate += v # Sum of numbers that don't fit.
                    
    print("Error rate: %d." % error_rate)
        
            
