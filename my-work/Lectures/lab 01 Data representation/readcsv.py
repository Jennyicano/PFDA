# simple program to read csv
# Author Jennifer Ibanez

import csv

FILENAME= "data.csv"
DATADIR = "../datafiles/"

# with open (DATADIR + FILENAME, "rt") as fp:
    # reader = csv.reader(fp, delimiter="," , quoting=csv.QUOTE_ALL)
    # for line in reader:
        # print(line)
    
with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter="," , quoting=csv.QUOTE_ALL)
    linecount = 0
    total = 0
    for line in reader:
        if not linecount:
            print (f"{line}\n---------------")
        else:
            total += int(line[0])
            print (line)
        linecount += 1
