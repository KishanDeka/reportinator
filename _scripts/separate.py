import os
import csv
import pandas as pd

# Clean out the process folder
os.system("rm ../_assets/process/*")
os.system("rm ../_assets/texts/*")

# Separate into numbers
with open("../_assets/input.txt", "r") as f:
    buff = []
    i = 1
    for line in f:
        if line.strip():  #skips the empty lines
           buff.append(line)
        if line.strip() == "%%":
           output = open('../_assets/process/%d.txt' % i,'w')
           output.write(''.join(buff))
           output.close()
           i+=1
           buff = [] #buffer reset

# Rename and remove
for file in os.listdir("../_assets/process"):
    with open ("../_assets/process/"+file, 'r') as f:
        data = f.read().splitlines(True)
        data = data[:-1]
        firstline = data[0]
        lastline = data[-1]
        title = firstline[2:-1]
        title = "../_assets/texts/"+title
    with open(title, 'w') as fout:
        fout.writelines(data[1:])

for file in os.listdir("../_assets/texts"):
    os.system("mv ../_assets/texts/"+file+" ../_assets/texts/"+file+".md")
    os.system("pandoc -f markdown -t latex ../_assets/texts/"+file+".md >> ../_assets/texts/"+file+".tex")
    os.system("rm ../_assets/texts/"+file+".md")
    os.system("mv ../_assets/texts/"+file+".tex "+"../_assets/texts/"+file)