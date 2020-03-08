## Almost done, but don't run, no fallback options edited in
import os
import pandas as pd
import csv
import argparse
import shutil
import sys

# Change working directory
script = str(os.path.dirname(os.path.realpath(sys.argv[0])))
os.chdir(script)

# Clean
shutil.rmtree("../tex_out", ignore_errors=True, onerror=None)
os.mkdir("../tex_out")

# Source Directory
parser = argparse.ArgumentParser(description='Welcome to Reportinator 1.0')
parser.add_argument('--source', required=True, help="Directory path of the source files, without / at the end")
args = parser.parse_args()
path = args.source

# EXTRACT FUNCTION
def extract(string, start='(', stop=')'):
    return string[string.index(start)+1:string.index(stop)]

# INCLUDE IMAGE FUNCTION
def image(source):
    with open(source, "r") as f:
        for line in f:
            content = line.strip()
            if content[:6] == "image(":
                file = content[content.index('(')+1:content.index(')')]
                os.system("python3 image.py --file "+file)    
            else:
                print (content)

# METADATA FUNCTION
def meta(x):
    with open ('../meta.csv') as f:
        data=list(csv.reader(f))
        return (data[1][x]) 

# GETTING DATA
os.system("python3 separate.py --file "+path)

# METADATA
data=list(csv.reader("../meta.csv"))
documentstyle = meta(2) # change for meta.csv
author = meta(0) # change for meta.csv
title = meta(3)

# MAKE FILE, CODE and CSV LISTS
source_csv = []
file_list = []
code_list = []
for file in os.listdir("../_assets/texts"):
    file_list.append(file)
file_list.sort()
for file in os.listdir("../_scripts"):
    code_list.append(file)
for file in os.listdir("../_assets/csvs"):
    source_csv.append(file)

# CODE FOR WRITING

print ("\\documentclass{../_layouts/"+documentstyle+"}\n")
print ("\\begin{"+"document}\n")
print ("\\title{"+title+"}\n")
print ("\\author{"+author+"}\n")
print ("\\date{"+"\\today"+"}")
print ("\\maketitle\n")

for file in file_list:
    ## We have the file[1:] to account for naming as 1Abc. The ordering is set by the numbering in front.
    
    # ABSTRACT
    if file[1:] == "Abstract:":
        name = file[1:] 
        print ("\\begin{"+"abstract"+"}")
        f = open("../_assets/texts/"+file, 'r')
        file_contents = f.read()
        print (file_contents)
        print ("\\end{"+"abstract"+"}")

    # TABLES
    elif file[1:] == "Observations:":
        name = file[1:] 
        print ("\\section{"+name+"}")
        for source in source_csv:
            if source != ".DS_Store":
                os.system("python3 tably.py ../_assets/csvs/" + source)    
            # figure out exactly
    elif file[1:] == "DS_Store":
        pass
    # GRAPHS
    elif file[1:] == "Graphs:":
        name = file[1:] 
        print ("\\section{"+name+"}")
        for source in source_csv:
            # read last line
            if source != ".DS_Store":
                csv_path = "../_assets/csvs/"+source
                with open (csv_path) as f:
                    data = f.readlines()
                lastline = data[-1]
                lastline = lastline.split(')')
                lastline = lastline[0]
                lastline = lastline[1:]+')'
                penline = data[-2]
                compare = lastline[:5]
                if compare == "graph":
                    graph = extract(lastline) #stuff between brackets
                    graph_list = []
                    #fitlist = extract(penline) #stuff between brackets
                    #fit_list = []
                    #fit_list = fitlist.split(',')
                    graph_list = graph.split(',')
                    i = 0
                    while i < len(graph_list):
                        #fitfun = fit_list[i]
                        X = graph_list[i]
                        Y = graph_list[i+1]
                        figure = "python3 figures.py --file ../_assets/csvs/"+source+" -x "+str(X)+" -y "+str(Y)#+" --fit "+fitfun
                        os.system(figure)
                        i+=2
            
    # NEW CODE AND REST   
    else:
        name = file[1:]
        print ("\\section{"+name+"}")
        path = "../_assets/texts/"+file
        image(path)
        if (file[1:]+".py" in code_list):
            code = "python3"+file[1:]+".py"
            os.system(code)
print ("\\end{document"+"}")