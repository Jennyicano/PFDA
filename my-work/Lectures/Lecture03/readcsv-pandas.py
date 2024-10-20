# reading in the CSV as a pandas table
# Following the lesson 1
# Author Jenny Ibanez

FILENAME= "data.csv"
DATADIR = "../datafiles/"

import pandas
df = pandas.read_csv(DATADIR + FILENAME)
print (df)

