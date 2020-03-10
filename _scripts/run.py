import os
import argparse
import sys
import shutil
import csv
import config

script = str(os.path.dirname(os.path.realpath(sys.argv[0])))
os.chdir(script)

def meta(x):
    with open ('../meta.csv') as f:
        data=list(csv.reader(f))
        return (data[1][x]) 

def ext(file,path):
    fp = "../_assets/"+file
    ext = os.path.splitext(fp)[-1].lower()
    if ext == ".pdf":
        shutil.copy("../_assets/"+file,path+"/"+file)

parser = argparse.ArgumentParser(description='Welcome to Reportinator 1.0')
parser.add_argument('--source', required=True, help="Directory path of the source files, without / at the end")
parser.add_argument('--reconfig', required=False, default=False, action="store_true", help="Run the reconfiguration script")

args = parser.parse_args()
path = args.source
pythonpath = sys.executable

#print(config.reconfig)
if config.reconfig or args.reconfig:
    print("Performing reconfiguration setup...")
    os.system(pythonpath+" setup.py")



# data=list(csv.reader("../meta.csv"))
# documentstyle = meta(2)
import config
documentstyle = config.style
print("Your LaTeX code is being processed. Please check your source directory")
os.system(pythonpath+" -u main.py --source "+path+" > ../report.tex")
shutil.copy("../report.tex", path+"/report.tex")
for file in os.listdir("../_assets/"):
    ext(file,path)
shutil.copy("../_layouts/"+documentstyle+".cls", path+"/"+documentstyle+".cls")
print("Your shit's sorted")
