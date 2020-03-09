import csv

def numcol(file):
    datafilename = '../_assets/csvs/'+file
    f=open(datafilename,'r')
    reader=csv.reader(f,delimiter=',')
    ncol=len(next(reader)) 
    f.seek(0)
    for row in reader:
        pass
    return ncol
