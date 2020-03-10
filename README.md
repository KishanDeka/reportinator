# Aim of the Project:
To make LaTeX reports easily from markdowns, containing the section data and marked CSVs. Please look at the example first, before doing anything.

## Installation:
Run `packages.sh` by running, and giving in your sudo password
```shell
bash packages.sh
```
Then clone the repo:
```shell
git clone "https://github.com/spandananupam/reportinator"
```
**For windows installation, please install Python 3.7+ and LaTeX, and use pip3 for all the pip packages written down in packages.sh**

## Basic Usage:
The whole code is activated in `_scripts/` by:
```shell
python3 run.py --source path/to/source/directory
```
For the first time only, the script will ask for default configuration options. The next time you want to reconfigure, you may run
```shell
python3 run.py --reconfig --source path/to/source/directory
```

For windows please make sure that your python version is up to date:
```shell
py run.py --source path/to/source/directory
```

## Dependencies:
For the sake of this project, these packages/programs have to be installed:
* Python 3.7 onwards
* LaTeX
* pandas
```shell
pip3 install pandas
```
* pypandoc
```shell
pip3 install pypandoc
```
* pandoc-xnos [install xnos](https://github.com/tomduck/pandoc-xnos/#Installation)

If there are any problems, please check if your python versions are correct, and then report issues

## File Structure:

`_scripts` contains all the code. If you want a custom code to run in a particular section, you need to keep your script with the name same as the the name of the section.

`_layouts` contains all the .cls files for LaTeX

`example_source` contains an example. Copy and paste this over to your favorite location and use the full address as the source tag while running `run.py`

## Input Markdown:
The name of the input markdown is the title of the report. Please do not use ":" at the end of your main headings.

The input markdown takes everything into LaTeX with the help of `pandoc`. Due to this, there are certain rules that have to be followed to prevent errors in the final output.
Recommended use: Typora, as a markdown editor, otherwise:

For recognizing multiple subsections, or lists with a text above them, it is necessary that you leave a one line gap between each subsection, or before the list. There is an example loaded in the current repo, which may be referred to, initially.
**Tables and Graphs will only be plotted only if the program sees the appropriate section headings.** If you are leaving some section like graphs blank, and want to only fill it up with python graphs, you need to leave one blank line in the section. That is, you must have atleast one line in each section, even if it is blank.

### Equations:
For putting in equations, you must type:
```markdown
$$ your-equation $$ {#eq:tag}
```
For referencing them anywhere inside the text, you just need to type `@eq:tag` or `{@eq:tag}` at the appropriate place.

### Images:
Example for inserting images into the markdown:
```markdown
image(name.png)
```
Refer to these images by saying {@fig:name} in-text.

### Tables:
All the csv files placed in the source folder will be converted to tables. For good looking reports, please make sure that there are a maximum of 4 columns, in double column.

### Graphs:
These are triggered by a graph statement at the end of the csvfile (Look at the example in example_source). They need to be in the first cell of the last row of the csvfile in a specific format. If you want the color scheme changed, there are 6 major color schemes inside `figures.py` that can be changed at will, or you may add your own.
```
graph(x,y,x,y..)
```
Where x,y pairs are column pairs that need to be plotted. Without this tag at the end of the csv, the table will only be passed as a table, and not into graphs.

## Advanced Usage (For Pros only):
If you want some special code to run in a specific section, then you might edit the corresponding existing code, or make a python code with the name same as the name of the section and place it in `_scripts/`. **Please note that in its current state, the name of the code is case sensitive. Name it exactly the same as your section heading**. If your code has some errors, it will print out to your tex code, or wont print at all.

## Templates
This code supports templates. All the class files are to be stored in `_layouts/`. Please add these lines to your custom class file, after `\NeedsTeXFormat{LaTeX2e}`:
```latex
 \usepackage[utf8]{inputenc}
 \usepackage{times}
 \usepackage{graphicx}
 \usepackage{amssymb}
 \usepackage{textcomp}
 \usepackage{gensymb}
 \usepackage{amsmath}
 \usepackage{float}
 \usepackage{booktabs}
 \usepackage[table,xcdraw]{xcolor}
 \providecommand{\tightlist}{%
   \setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
```
The graph python code uses seaborn, you may look at the different styles available in the internet for the same, and change it in `_scripts/figures.py`

# To do:
* Fitting in the graph

# Example:
One example has been given in the program at `example_source`
