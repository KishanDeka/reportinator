import csv

with open ('../meta.csv') as f:
    data=list(csv.reader(f))
    print (data[1][0])
