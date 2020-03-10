import os
import sys
import fileinput

script = str(os.path.dirname(os.path.realpath(sys.argv[0])))
os.chdir(script)

name = input("Enter name: ")
affiliation = input("Enter affiliation: ")
style = input("Enter name of the custom class file (Leave blank for default): ")


for line in fileinput.input("config.py", inplace=True):
    if line != "":
        if line[:5] == "name=":
            print('{}"{}"'.format("name=", name))
        elif line[:12] == "affiliation=":
            print('{}"{}"'.format("affiliation=", affiliation))
        elif line[:6] == "style=":
            if style != "":
                print('{}"{}"'.format("style=", style))
            else:
                print('{}"{}"'.format("style=", "ieeeconf"))
        elif line[:9] == "reconfig=":
            print('{}{}'.format("reconfig=", "False"))
        else:
            print(line)
    else:
        pass



