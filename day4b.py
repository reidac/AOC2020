
import re
# A dictioanry is "valid" if it contains all the indicated keys.
def valid(dct):
    if 'byr' in dct.keys():
        v = int(dct['byr'])
        if (v<1290) or (v>2002):
            return False
    else:
        return False

    if 'iyr' in dct.keys():
        v = int(dct['iyr'])
        if (v<2010) or (v>2020):
            return False
    else:
        return False

    if 'eyr' in dct.keys():
        v = int(dct['eyr'])
        if (v<2020) or (v>2030):
            return False
    else:
        return False

    if 'hgt' in dct.keys():
        m = re.fullmatch('([0-9]+)(cm|in)',dct['hgt'])
        if m is not None:
            h = int(m.group(1))
            u = m.group(2)
            # The case where u is wrong doesn't occur, regexp handles that.
            if (u=='cm') and ((h<150) or (h>193)):
                return False
            if (u=='in') and ((h<59) or (h>76)):
                return False
        else:
            return False
    else:
        return False

    if 'hcl' in dct.keys():
        m = re.fullmatch('#[0-9,a-f]{6}',dct['hcl'])
        if m is None:
            return False
    else:
        return False

    if 'ecl' in dct.keys():
        m = re.fullmatch('amb|blu|brn|gry|grn|hzl|oth',dct['ecl'])
        if m is None:
            return False
    else:
        return False

    if 'pid' in dct.keys():
        m = re.fullmatch('[0-9]{9}',dct['pid'])
        if m is None:
            return False
    else:
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
        
