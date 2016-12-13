import sys
import glob         #get files
import errno
import re

path = str(sys.argv[-1])+"*.txt"   #directory name
files = glob.glob(path)

# +91-xxx yyy zzzz
regex = "(?:(?:\+|0{0,2})91(\s*[\\-]\s*)?|[0]?)?[789]\d{2}\s*\d{3}\s*\d{4}"

for name in files:
    try:
        with open(name) as f:
            #print "file : %s"%name
            lines = f.read()
            matches = re.finditer(regex, lines)
            for match in matches:
                print ("{match}".format(match = match.group()))

    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise
