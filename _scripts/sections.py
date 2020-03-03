import os
file_list = []
for file in os.listdir("../_assets/texts"):
    file_list.append(file)
file_list.sort()
print (file_list)

for file in file_list:

    if file[1:] == "Observations":
        with open('_outputs/sections.txt', 'a') as f:
            name = file[1:] 
            print ("\\section{"+name+"}",file=f)
        # code for table
        print ("a")
    elif file[1:] == "Graphs":
        with open('_outputs/sections.txt', 'a') as f:
            name = file[1:] 
            print ("\\section{"+name+"}",file=f)
        # code for graphs

    else:
        with open('_outputs/sections.txt', 'a') as f:
            name = file[1:] 
            print ("\\section{"+name+"}",file=f)
        f = open("../_assets/texts/"+file, 'r')
        file_contents = f.read()
        with open('_outputs/sections.txt', 'a') as f:
            print (file_contents)