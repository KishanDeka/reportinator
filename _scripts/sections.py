import os
import pandas as pd

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
#i = 1

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
        with open('_outputs/sections.txt', 'a') as f:
            name = file[1:] 
            print ("\\section{"+name+"}",file=f)
        for source in source_csv:
            while n < N:
                figure = "python figures.py --file " + source + " -x " + X[n] + " -y " + Y[n]
                exec(figure)
                n = n+1
            
            

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
