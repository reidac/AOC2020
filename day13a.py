

if __name__=="__main__":
    f = open("day13.txt","r")
    l1 = f.readline()
    arrival_time = int(l1)
    l2 = f.readline()
    minwait = None
    minid = None
    for x in l2.split(','):
        try:
            freq = int(x)
        except ValueError:
            pass
        else:
            wtime = freq - (arrival_time % freq)
            if (minwait is None) or (wtime < minwait):
                minwait = wtime
                minid = freq

    print("Id of earliest bus: %d" % minid)
    print("Wait time: %d" % minwait)
    print("Actual answer: %d." % (minid*minwait))
