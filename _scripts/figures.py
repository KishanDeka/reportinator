#using seaborn as stylesheet https://python-graph-gallery.com/106-seaborn-style-on-matplotlib-plot/
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import argparse
import sys
import random

plt.style.use('bmh')
palette = []
deep=["#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B3","#937860", "#DA8BC3", "#8C8C8C", "#CCB974", "#64B5CD"]
deep6=["#4C72B0", "#55A868", "#C44E52","#8172B3", "#CCB974", "#64B5CD"]
muted=["#4878D0", "#EE854A", "#6ACC64", "#D65F5F", "#956CB4","#8C613C", "#DC7EC0", "#797979", "#D5BB67", "#82C6E2"]
muted6=["#4878D0", "#6ACC64", "#D65F5F","#956CB4", "#D5BB67", "#82C6E2"]
pastel=["#A1C9F4", "#FFB482", "#8DE5A1", "#FF9F9B", "#D0BBFF","#DEBB9B", "#FAB0E4", "#CFCFCF", "#FFFEA3", "#B9F2F0"]
pastel6=["#A1C9F4", "#8DE5A1", "#FF9F9B","#D0BBFF", "#FFFEA3", "#B9F2F0"]
bright=["#023EFF", "#FF7C00", "#1AC938", "#E8000B", "#8B2BE2","#9F4800", "#F14CC1", "#A3A3A3", "#FFC400", "#00D7FF"]
bright6=["#023EFF", "#1AC938", "#E8000B","#8B2BE2", "#FFC400", "#00D7FF"]
dark=["#001C7F", "#B1400D", "#12711C", "#8C0800", "#591E71","#592F0D", "#A23582", "#3C3C3C", "#B8850A", "#006374"]
dark6=["#001C7F", "#12711C", "#8C0800","#591E71", "#B8850A", "#006374"]
colorblind=["#0173B2", "#DE8F05", "#029E73", "#D55E00", "#CC78BC","#CA9161", "#FBAFE4", "#949494", "#ECE133", "#56B4E9"]
colorblind6=["#0173B2", "#029E73", "#D55E00","#CC78BC", "#ECE133", "#56B4E9"]
black=['ffffff']

# CHOOSE PALETTE
palette=dark

# parser
parser = argparse.ArgumentParser(description='Program for plotting and fitting figures for laTex reportinator 1.0')
parser.add_argument('--file', required=True, help="Input the name of the csv file to be converted into a figure, placed in assets")
parser.add_argument('-x', required=True, help="Input the column number for x")
parser.add_argument('-y', required=True, help="Input the column number for y")
# parser.add_argument('--fit', required=False, help="Input the fit function")
args = parser.parse_args()
file = args.file
#inputs and initializations
in_file = "../_assets/csvs/"+args.file
x_index = int(args.x) - 1
y_index = int(args.y) - 1
data = pd.read_csv(in_file)
data = data[:-1]
x_name = data.columns[x_index]
y_name = data.columns[y_index]
in_x = 0
in_y = 0
#fun = args.fit

#actual plotting and saving in PDF
def plot(x_name, y_name, data):
    x = data[x_name]
    x = list(map(float, x))
    y = data[y_name]
    y = list(map(float, y))
    f = plt.figure()
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.plot (x,y, linestyle="dotted", marker = "o",
            color=random.choice(palette), label="Observed Data")
    plt.xlabel(r'%s' % x_name,fontsize = 13)
    plt.ylabel(r'%s'% y_name,fontsize = 13)
    plt.legend()
    f.savefig("../_assets/"+y_name.split(" ")[0]+".pdf", bbox_inches = 'tight')
    return y_name

file_name = file[:-4]

def pregraph(name):
    location = "./"+name.split(" ")[0]+".pdf"
    tag = name.split(" ")[0]
    tag_new = tag.lower()
    print ('\\begin{figure}[H]'+'\n'+'\\centering'+'\n'+'\\includegraphics[width = \\columnwidth]'+'{'+location+'}'+'\n'+'\\caption{'+tag+'}'+'\n'+'\\label{fig:\"'+tag_new+'\"}'+'\n'+'\\end{figure}')
    return 0
# def fit():
#     if fun == "expo":
#         func.expo()
#     elif fun == "lin":
#     elif fun == "pol2":
#     elif fun == "pol3":
#     elif fun == "pol4":
#     elif fun == "pol5":
#     elif fun == "log":
#     else:
#         print("Wrong function")

# if fun:
#     (xf, yf), params, err, chi = fit(fun)
#     print ("N:    %.2f +/- %.3f" % (params[0], err[0]))
#     print ("N:    %.2f +/- %.3f" % (params[1], err[1]))
#     print ("N:    %.2f +/- %.3f" % (params[2], err[2]))
#     plot(x_name, y_name, data)
#     plt.plot(xf, yf, 'r-', label="Fitted Data")
#     legend()

# else:
y_name = plot(x_name, y_name, data)
pregraph(y_name)


