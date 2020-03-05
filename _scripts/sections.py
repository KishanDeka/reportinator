## Almost done, but don't run
import os
import pandas as pd
import csv

# METADATA
documentstyle = "ieeeconf" #change for meta.csv
author = "Spandan Anupam" #change for meta.csv

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

print ("\\documentstyle{../_layouts/"+documentstyle+"}\n")
print ("\\author{"+author+"}\n")
print ("\\date{"+"\\today"+"}")

for file in file_list:
    ## We have the file[1:] to account for naming as 1Abc. The ordering is set by the numbering in front.
    
    # ABSTRACT
    if file[1:] == "Abstract":
        with open('_outputs/sections.txt', 'a') as f:
            name = file[1:] 
            print ("\\begin{"+name+"}")
        f = open("../_assets/texts/"+file, 'r')
        file_contents = f.read()
        with open('_outputs/sections.txt', 'a') as f:
            print (file_contents)

    # TABLES
    if file[1:] == "Observations":
        with open('_outputs/sections.txt', 'a') as f:
            name = file[1:] 
            print ("\\section{"+name+"}")
        for source in source_csv:
            exec("python tably.py source --tags")    
            # figure out exactly

    # GRAPHS
    elif file[1:] == "Graphs":
        if file[1:] == "Graphs":
            with open('_outputs/sections.txt', 'a') as f:
                name = file[1:] 
                print ("\\section{"+name+"}")
        for source in source_csv:
            # read last line
            csv_path = "../assets/csvs"+source
            with open (csv_path) as f:
                data = f.readlines()
            lastline = data[-1]
            # alt
            # for line in open('logfile.txt'):
            #     pass
            # print(line)
            compare, graph = lastline[:6], lastline[6:]
            graph = graph[:-1]
            graph_list = []
            if compare == "graph(":
                graph_list = graph.split(',')
                i = 0
                while i < len(graph_list):
                    X = graph_list[i]
                    Y = graph_list[i+1]
                    figure = "python figures.py --file "+source+" -x "+X+" -y "+Y
                    exec(figure)
                    i+=2
            

    # NEW CODE AND REST   
    else:
        with open('_outputs/sections.txt', 'a') as f:
            name = file[1:]
            print ("\\section{"+name+"}",file=f)
        f = open("../_assets/texts/"+file, 'r')
        file_contents = f.read()
        with open('_outputs/sections.txt', 'a') as f:
            print (file_contents)
        if (file[1:]+".py" in code_list):
            code = "python"+file[1:]+".py"
            exec(code)