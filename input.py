#!/usr/bin/python3

#
# Get session data from the browser. In chrome, click on
# the padlock icon, then "Cookies", then on the 
# domain (adventofcode.com), then find the one
# named "session", and copy out the "content":

# NB auto-downloads are strongly discouraged by the 
# devs, but once a day is OK.

import sys
import requests
import getopt
from datetime import date

if __name__=="__main__":

    defaultday = int(date.today().strftime("%d"))
    day = defaultday

    try:
        opts, args = getopt.getopt(sys.argv[1:],'d:')
    except getopt.GetoptError as e:
        print(e)
        print('The only option is "-d <day>", defaults to today.')
        sys.exit(64)

    for o,a in opts:
        if o=='-d':
            day = int(a)

    print("Downloading for day %d." % day)

    f = open("session.txt","r")
    session_data = f.read()[:-1]  # Trailing newline.

    r = requests.get("https://adventofcode.com/2020/day/%d/input" % day,
                     cookies={"session": session_data })
    f = open("day%d.txt" % day,"w")
    f.write(r.text)
    f.close()
