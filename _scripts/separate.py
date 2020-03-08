import os
import csv
import pandas as pd
import shutil
import argparse

# Parse source
parser = argparse.ArgumentParser(description='Program for processing text and assets for reportinator 1.0')
parser.add_argument('--file', required=True, help="Input the name of the csv file to be converted into a figure, placed in assets")
args = parser.parse_args()
source = args.file

# Extension helper: https://stackoverflow.com/questions/5899497/how-can-i-check-the-extension-of-a-file
def ext(fp):
    ext = os.path.splitext(fp)[-1].lower()
    if ext == ".csv":
        return ("csv")
    elif ext == ".md":
        return ("md")
    else:
        return ("something")

# Make new directories 
shutil.rmtree("../_assets", ignore_errors=True, onerror=None)
os.mkdir('../_assets')
os.mkdir('../_assets/process')
os.mkdir('../_assets/texts')
os.mkdir('../_assets/csvs')

# Copy over contents 
for file in os.listdir(source):
    path = source+'/'+file
    if file == "meta.csv":
        shutil.copy(path,'../meta.csv')
    elif ext(path) == "csv" and file != "meta.csv":
        shutil.copy(path,'../_assets/csvs/'+file)
    elif ext(path) == "md":
        shutil.copy(path,'../input.md')       
    else:
        shutil.copy(path,'../_assets/'+file)

# Separate into numbers
with open("../input.md", "r") as f:
    buff = []
    i = 1
    for line in f:
        #if line.strip():  #skips the empty lines
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
    shutil.copy("../_assets/texts/"+file, "../_assets/texts/"+file+".md")
    os.system("pandoc -f markdown-auto_identifiers --filter pandoc-eqnos --wrap=preserve -t latex ../_assets/texts/"+file+".md >> ../_assets/texts/"+file+".tex")
    os.remove("../_assets/texts/"+file+".md")
    shutil.copy("../_assets/texts/"+file+".tex", "../_assets/texts/"+file)
    os.remove("../_assets/texts/"+file+".tex")