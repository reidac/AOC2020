import re

# A bag knows its name, and how many of what other-named bags
# it can directly contain.
class Bag:
    def __init__(self,name):
        self.name = name
        self.contents = {}
    def add_sub(self,number,name):
        self.contents[name]=number
    def __repr__(self):
        return "Bag(%s)" % self.name
        
if __name__=="__main__":
    bdict = {}
    f = open("day7.txt","r")
    for ln in f:
        l = ln[:-1] # Get it? Removes the \n.
        ss = l.split(',')
        m1 = re.search('([ a-z]+) bags contain (.*)',ss[0])
        bg = Bag(m1.group(1))
        if (m1.group(2)[0:2]!="no"):
            m2 = re.search('([0-9]+) ([ a-z]+) bag',m1.group(2))
            bg.add_sub(int(m2.group(1)),m2.group(2))
            for other in ss[1:]:
                m3 = re.search(' ([0-9]+) ([ a-z]+) bag',other)
                bg.add_sub(int(m3.group(1)),m3.group(2))
        bdict[bg.name] = bg

    # So at this point we have a dictionary of bag objects which
    # knows the containment hierarchy.  What was the question?
    
    # How many bag colors can contain a shiny gold bag, to
    # all orders?

    # Invert the map. Keys are contained bags, values are
    # lists of containing bags.
    containing = {}
    for (k,v) in bdict.items():
        for c in v.contents.keys():
            try:
                containing[c].append(k)
            except KeyError:
                containing[c]=[k]

    search_set = set(["shiny gold"])
    found_set = set()
    done = False
    while not done:
        fss = len(found_set)
        new_search_set = set()
        for k in search_set:
            try:
                vs = containing[k] # Some bags are not contained!
            except KeyError:
                pass
            else:
                for v in vs:
                    found_set.add(v)
                    new_search_set.add(v)
        if len(found_set)==fss: # No new items, we are done.
            done = True
        else:
            search_set = new_search_set

    print("Done, size is %d." % len(found_set))
    
