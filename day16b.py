import re

if __name__=="__main__":
    f = open("day16.txt")
    range_dict = {}
    error_rate = 0
    my_ticket = None
    valid_tickets = []
    nearby_tickets_seen = False
    for ln in f:
        m = re.search('^(.*): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)',ln)
        if m:
            datum = m.group(1)
            range1 = (int(m.group(2)),int(m.group(3)))
            range2 = (int(m.group(4)),int(m.group(5)))
            range_dict[datum] = [range1,range2]

        # All ranges are specified before any tickets are seen.

        m = re.search('nearby tickets:',ln)
        if m:
            nearby_tickets_seen = True
            
        m = re.search('^(([0-9]+),)+[0-9]+',ln)
        if m:
            vals = list(map(int,re.findall('[0-9]+',ln)))
            if not (nearby_tickets_seen):
                my_ticket = vals
            else:
                t_valid = True
                for v in vals:
                    v_valid = False
                    for rl in range_dict.values():
                        for rng in rl:
                            if (v>=rng[0]) and (v<=rng[1]):
                                v_valid = True
                                break
                        if v_valid:
                            break
                    if (t_valid) and not (v_valid):
                        t_valid = False
                        break
                if t_valid: # Every entry fits in somewhere.
                    valid_tickets.append(list(vals))
                    
    # At this point, we have a list, valid_tickets, of tickets
    # for which every number fits in to some range or other.
    
    # Now figure out the slots.
    nslots = len(my_ticket)
    all_slots = set()
    for k in range_dict.keys():
        all_slots.add(k)
    candidates = [all_slots.copy() for i in range(nslots)]

    for tkt in valid_tickets:
        for slot in range(len(tkt)):
            removal_list = []
            v = tkt[slot]
            for cat in candidates[slot]:
                rset = range_dict[cat]
                if (((v<rset[0][0]) or (v>rset[0][1]))
                    and ((v<rset[1][0]) or (v>rset[1][1]))):
                    removal_list.append(cat)
            for rm in removal_list:
                candidates[slot].remove(rm)

    # Now we have "reduced candidates" constrained by the ranges.
    # We can reduce further by successive elimination.

    resolved = set()
    done = False
    while not done:
        # Find all the singletons we haven't seen before.
        singletons = set()
        for c in candidates:
            if len(c)==1:
                cc = c.copy() # Better way to do this? Want to preserve c.
                cv = cc.pop()
                if cv not in resolved:
                    singletons.add(cv)
        if len(singletons)==0:
            done = True
        else:
            for c in candidates:
                if len(c)!=1:
                    for s in singletons:
                        c.discard(s)
            resolved.update(singletons)

    # OK, we have unique IDs for each slot.
    res = 1
    for i in range(len(candidates)):
        for cv in candidates[i]: # Only one iteration.
            if cv[0:9]=="departure":
                res *= my_ticket[i]

    print("Result: %d." % res)

            
