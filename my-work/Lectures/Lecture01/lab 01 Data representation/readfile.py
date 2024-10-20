# Week 1
# read a file
# practising while following the lecture 1
# Author: Jenny Ibanez

FILENAME = "data.txt"
DATADIR = "../datafiles/"

print(DATADIR + FILENAME)

with open(DATADIR + FILENAME, "rt") as fp:
    total = 0
    for line in fp:
        total += int(line) # the text needs to be onverter to int
        print (f"{line} is size {len(line)}")
    print (total) 
    print (f"total is {total}")