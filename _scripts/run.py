import os
import argparse
import sys
import shutil
import csv
import config

wd = os.getcwd()
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
    else:
        return ext

parser = argparse.ArgumentParser(description='Welcome to Reportinator 1.0')
parser.add_argument('--source', required=False, default=False, help="Directory path of the source files, without / at the end")
parser.add_argument('--reconfig', required=False, default=False, action="store_true", help="Run the reconfiguration script")

args = parser.parse_args()
if not args.source:
    path = wd
else:
    path = args.source
pythonpath = sys.executable

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
os.remove("../report.tex")
for file in os.listdir("../_assets/"):
    ext(file,path)
shutil.copy("../_layouts/"+documentstyle+".cls", path+"/"+documentstyle+".cls")
shutil.rmtree("../_assets", ignore_errors=True, onerror=None)
shutil.rmtree("../_scripts/__pycache__", ignore_errors=True, onerror=None)
os.chdir(path)
os.system("pdflatex report.tex && latexmk -c")
print("Your shit's sorted")
