# simple program to read csv
# Author Jennifer Ibanez

import csv

FILENAME= "data.csv"
DATADIR = "../datafiles/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter="," , quoting=csv.QUOTE_ALL)
    for line in reader:
        print(line)
    