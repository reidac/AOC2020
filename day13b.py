

if __name__=="__main__":
    f = open("day13.txt","r")
    l1 = f.readline()
    arrival_time = int(l1)
    l2 = f.readline()

    dep_dict = {}
    dep_list = []
    dep_count = 0
    for x in l2.split(','):
        try:
            freq = int(x)
        except ValueError:
            pass
        else:
            dep_dict[dep_count]=freq
            dep_list.append(dep_count)
        dep_count += 1

    # print(dep_dict)
    # print(dep_list)
    
    # Goal-state detection.
    # dtime = 1068781
    # for (k,v) in dep_dict.items():
    #     print("Check: %d %d." % (k, (dtime+k)%v) )

    # Induction scheme.
    # Find the answer for the first pair, then increment along
    # successive first-pair answers until new data is satisifed,
    # and proceed by induction.
    res = dep_dict[dep_list[0]]
    prd = dep_dict[dep_list[0]]
    for v in dep_list[1:]:
        done = False
        while not done:
            res += prd
            if (res+v)%dep_dict[v]==0:
                prd *= dep_dict[v]
                done = True

    print("Result: %d." % res)
