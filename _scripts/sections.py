## !!Incomplete, wont work!!

import os
import pandas as pd
import csv

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

tables_config = pd.read_csv("../_assets/tables_config.csv")

# CODE FOR WRITING
for file in file_list:

    # TABLES
    if file[1:] == "Observations":
        with open('_outputs/sections.txt', 'a') as f:
            name = file[1:] 
            print ("\\section{"+name+"}",file=f)
        for source in source_csv:
            exec("python tably.py source --tags")    
            # figure out exactly

    # GRAPHS
    elif file[1:] == "Graphs":
        if file[1:] == "Graphs":
            with open('_outputs/sections.txt', 'a') as f:
                name = file[1:] 
                print ("\\section{"+name+"}",file=f)
        for file in source_csv:
            # read last line
            csv_path = "../assets/csvs"+file
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
                    figure = "python figures.py --file "+file+" -x "+X+" -y "+Y
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
