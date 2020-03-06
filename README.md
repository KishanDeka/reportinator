# Reportinator
Aim: To make and mail beautiful reports written in latex, with the help of `tably` and some hand written code.

## Usage:
This project is still under construction, and will take some days to get to its full functional capacity. 
Almost all of the python scripts are done, and will be up in a few days. The current implementation calls for the text to be written in `_assets/input.txt.`
There is a specific format for the text to be written, that looks something like this:

```shell
1Abstract:
abc
;
2Introduction
def
;
3Observations
ghi
;
4Graphs
jkl
;
5Conclusion
asfasf
;
```

Right now, the help section of `figures.py` is active. It can be turned on by:
```shell
cd download_dir/reportinator/_scripts/
python figures.py --help
```
The actual help section for lazybums:
```console
usage: figures.py [-h] --file FILE -x X -y Y

Program for plotting and fitting figures for LaTex reportinator 1.0

optional arguments:
  -h, --help   show this help message and exit
  --file FILE  Input the name of the csv file to be converted into a figure, placed in assets
  -x X         Input the column number for x
  -y Y         Input the column number for y
```
### Assets:
Will contain all the text files, containing the individual text blocks for the actual content, and the CSV files of the data taken.

### Layouts:
Will contain the latex templates which can be used for different purposes

### Scripts:
Will contain whatever there is, running the program.

Ideally, the final program should run automatically if we just put in data into a config file saying what graphs you need, and what columns the data is in. The program should just spit out the PDF file into the designated folder for each experiment.

## To Do List:
- Completion and adaption of tably by [narimiran](https://github.com/narimiran/tably)
- Completion of the config script taking initial configuration from the user
- Individual class files for easy use
- Data management and automation
- Fit functions
