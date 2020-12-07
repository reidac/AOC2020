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

def subbags(bdict,name):
    bg = bdict[name]
    if len(bg.contents)==0:
        return 0
    else:
        res = 0
        for (nm,ct) in bg.contents.items():
            res += ct + ct*subbags(bdict,nm)
    return res
    
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


    # Q: How many individual bags must a "shiny gold" bag contain?
    ans = subbags(bdict,"shiny gold")
    #
    # Happily, mindless recursion actually works, and terminates.
    print("Sub-bag answer: %d." % ans)
    
