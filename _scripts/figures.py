#using seaborn as stylesheet https://python-graph-gallery.com/106-seaborn-style-on-matplotlib-plot/
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import argparse

plt.style.use('seaborn-ticks')


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
x_name = data.columns[x_index]
y_name = data.columns[y_index]
in_x = 0
in_y = 0
#fun = args.fit

#actual plotting and saving in PDF
def plot(x_name, y_name, data):
    x = data[x_name]
    y = data[y_name]
    f = plt.figure()
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.plot (x,y,linestyle = "dashed", marker = "o", label="Observed Data")
    plt.xlabel(r'%s' % x_name,fontsize = 13)
    plt.ylabel(r'%s'% y_name,fontsize = 13)
    plt.legend()
    f.savefig("../_assets/"+y_name.split(" ")[0]+".pdf", bbox_inches = 'tight')
    return y_name

file_name = file[:-4]

def pregraph(name):
    location = "../_assets/"+name.split(" ")[0]+".pdf"
    print ('\\begin{figure}[H]'+'\n'+'\\centering'+'\n'+'\\includegraphics[width = \\columnwidth]'+'{'+location+'}'+'\n'+'\\caption{'+file_name+'}'+'\n'+'\\label{\"fig:'+file_name+'\"}'+'\n'+'\\end{figure}')
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
plot(x_name, y_name, data)
pregraph(y_name)


