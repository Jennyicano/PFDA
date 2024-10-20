# simple program to read csv file as a dictionary
# Author Jennifer Ibanez

import csv

FILENAME= "data.csv"
DATADIR = "../datafiles/"

# with open (DATADIR + FILENAME, "rt") as fp:
    # reader = csv.reader(fp, delimiter="," , quoting=csv.QUOTE_ALL)
    # for line in reader:
        # print(line)
    
with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter="," , quoting=csv.QUOTE_ALL)
    total = 0
    for line in reader:
        total += int(line['id'])
        print (line)
