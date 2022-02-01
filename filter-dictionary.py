#!/usr/bin/python3

import sys


f = open(sys.argv[1])

while (line := f.readline()):
    line = line.strip();
    idx = line.find("'")

    # ignore possessives 
    if (idx > -1):
        continue
    # end if

    # ignore proper nouns
    if (line[0].isupper()):
        continue
    # end if
    
    # accept only 5 letter words
    if (len(line) != 5):
        continue
    # end if

    # skip non-ascii characters and ignore the word if the
    # length changes
    non_ascii = line.encode("ascii", "ignore").decode()

    if (non_ascii != line):
        continue
    # end if
    
    print(line.upper())
# end while



f.close();
