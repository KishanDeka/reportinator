import os
import csv
import pandas as pd

# Clean out the process folder
exec("rm ../_assets/process/*")
exec("rm ../_assets/texts/*")

# Separate into numbers
with open("../_assets/input.txt", "r") as f:
    buff = []
    i = 1
    for line in f:
        if line.strip():  #skips the empty lines
           buff.append(line)
        if line.strip() == ";":
           output = open('../_assets/process/%d.txt' % i,'w')
           output.write(''.join(buff))
           output.close()
           i+=1
           buff = [] #buffer reset

# Rename and remove
for file in os.listdir("../_assets/process"):
    with open (file, 'r') as f:
        data = f.read().splitlines(True)
        firstline = f.readline()
        title = firstline[:-1]
        title = "../assets/texts/"+title
    with open(title, 'w') as fout:
        fout.writelines(data[1:])
