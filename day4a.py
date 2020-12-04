
import re
# A dictioanry is "valid" if it contains all the indicated keys.
def valid(dct):
    kset = ['byr','iyr','eyr','hgt','hcl','ecl','pid'] # 'cid' optional.
    for k in kset:
        if k not in dct.keys():
            return False
    return True
    
if __name__=="__main__":
    f = open("day4.txt","r")
    vcount = 0
    dct = {}
    for l in f:
        s = l[:-1] # Trailing newline.
        if len(s)==0:
            if valid(dct):
                vcount += 1
            dct = {}
        else:
            ss = s.split()
            for entry in ss:
                m = re.search('(.*):(.*)',entry)
                dct[m.group(1)]=m.group(2)
                
    if (dct): # Trailing un-processed dictionary.
        if valid(dct):
            vcount += 1
        dct = {}
                
    print("Valid entries: %d." % vcount)
        
