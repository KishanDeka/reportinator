# Aim of the Project:
To make LaTeX reports easily from markdowns, containing the section data and marked CSVs. Current implementation spits out the LaTeX code into `stdout`. **!! This project is in no way complete in its current state, please do not expect a lot !!**. I am working on making this project cross platform, it will soon be. Please look around first, before doing anything.

##
Clone this repository:
```shell
git clone "https://github.com/spandananupam/reportinator"
```

## Basic Usage:
You can edit the basic configurations in `meta.csv`. The whole code is activated in `_scripts/` by:
```shell
python main.py --source path/to/source/directory
```

## Dependencies:
For the sake of this project, these packages/programs have to be installed:
* Python 3.7 onwards
* LaTeX
* Pandoc (To be installed through the pandoc website, not through pip pypandoc as of now, on all platforms)
* Pandoc-Eqnos
```shell
pip install pandoc-eqnos
```
* shutil
If there are any problems, please check if your python versions are correct.

## File Structure:
`input.md` is the Input markdown (Please look at the example given by default)

`meta.csv` is the metadata required for each report.

`_assets` contains csv files, images, and files that are being processed.
* `csvs` contains all the csv files (Please look at the example given by default)
* `process` and `texts` are to be ignored by the average user

`_scripts` contains all the code. If you want a custom code to run in a particular section, you need to keep your script with the name same as the the name of the section.

`_old` is to be ignored

`_layouts` contains all the .cls files for LaTeX

`tex_out` is supposed to be the processing place for everything .tex.

## Input Markdown:
The input markdown takes everything into LaTeX with the help of `pandoc`. Due to this, there are certain rules that have to be followed to prevent errors in the final output.
Recommended use: Typora, as a markdown editor, otherwise:

For recognizing multiple subsections, or lists with a text above them, it is necessary that you leave a one line gap between each subsection, or before the list. There is an example loaded in the current repo, which may be referred to, initially.
**Tables and Graphs will only be plotted only if the program sees the appropriate section headings.**

### Equations:
For putting in equations, you must type:
```markdown
$$ your-equation $$ {#eq:tag}
```
For referencing them anywhere inside the text, you just need to type `@eq:tag` or `{@eq:tag}` at the appropriate place.
More: [pandoc-eqnos]('https://github.com/tomduck/pandoc-eqnos')

### Images:
Example for inserting images into the markdown:
```markdown
image(name.png)
```
### Tables:
Tables are made from csvs placed in `_assets/csvs/`. All the csv files placed here will be converted to tables. For good looking reports, please make sure that there are a maximum of 4 columns.

### Graphs:
Graphs are made from csv files placed in `_assets/csvs/`. These are triggered by a graph statement at the end of the csvfile. They need to be in the first cell of the last row of the csvfile in a specific format.
```
graph(x,y,x,y..)
```
Where x,y pairs are column pairs that need to be plotted. Without this tag at the end of the csv, the table will only be passed as a table, and not into graphs.

## Templates
This code supports templates. All the class files are to be stored in `_layouts/`. Please add these lines to your custom class file, after `\NeedsTeXFormat{LaTeX2e}`:
```latex
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
* All in one code for running the python script, and outputting into a tex file, and compiling.

# Example:
One example has been loaded by default into this program. Please see it, before erasing out anything.
