# Aim of the Project:
To make LaTeX reports easily from markdowns, containing the section data and marked CSVs. Current implementation spits out the LaTeX code into `stdout`.

## Dependencies:
For the sake of this project, these packages/programs have to be installed:
* Python 3+
* Pandoc
* Pandoc-Eqnos
```shell
pip install pandoc-eqnos
```

## Input Markdown:
The input markdown takes everything into LaTeX with the help of `pandoc`. Due to this, there are certain rules that have to be followed to prevent errors in the final output.
For recognizing multiple subsections, or lists with a text above them, it is necessary that you leave a one line gap between each subsection, or before the list.

### Equations:
For putting in equations, you must type:
```markdown
$$ your-equation $$ {#eq:tag}
```
For referencing them anywhere inside the text, you just need to type @eq:tag or {@eq:tag} at the appropriate place.
More: [pandoc-eqnos]('https://github.com/tomduck/pandoc-eqnos')

### Images:
Example for inserting images into the markdown:
```markdown
![la lune](lalune.jpg "Voyage to the moon")
```
### Tables:
Tables are made from csvs placed in `_assets/csvs/`. All the csv files placed here will be converted to tables. For good looking reports, please make sure that there are a maximum of 4 columns.

### Graphs:
Graphs are made from csv files placed in `_assets/csvs/`. These are triggered by a graph statement at the end of the csvfile. They need to be in the first cell of the last row of the csvfile in a specific format.
```
graph(x,y,x,y..)
```
Where x,y pairs are column pairs that need to be plotted. Without this tag at the end of the csv, the table will only be passed as a table, and not into graphs.




