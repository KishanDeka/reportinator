\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{multi}[2020/03/03 Class for multicolsreports]
\LoadClass[a4paper, 10pt, conference]{ieeeconf}
\overrideIEEEmargins
\makeatletter
\let\NAT@parse\undefined
\makeatother
\usepackage[dvipsnames]{xcolor}
\newcommand*\linkcolours{ForestGreen}
\usepackage{times}
\usepackage{graphicx}
\usepackage{amssymb}
\usepackage{gensymb}
\usepackage{amsmath}
\usepackage{breakurl}
\def\UrlBreaks{\do\/\do-}
\usepackage{url,hyperref}
\hypersetup{
colorlinks,
linkcolor=\linkcolours,
citecolor=\linkcolours,
filecolor=\linkcolours,
urlcolor=\linkcolours}
\usepackage{algorithm}
\usepackage{algorithmic}
\usepackage[labelfont={bf},font=small]{caption}
\usepackage[none]{hyphenat}
\usepackage{mathtools, cuted}
\usepackage[noadjust, nobreak]{cite}
\def\citepunct{,\,} % Style file defaults to listing references separately
\usepackage{tabularx}
\usepackage{amsmath}
\usepackage{float}
\usepackage{pifont}% http://ctan.org/pkg/pifont
\newcommand{\cmark}{\ding{51}}%
\newcommand{\xmark}{\ding{55}}%
\newcommand*\diff{\mathop{}\!\mathrm{d}}
\newcommand*\Diff[1]{\mathop{}\!\mathrm{d^#1}}
\newcommand*\imgres{600}
\newcommand*\GitHubLoc{https://github.com/Jeffrey-Ede/ALRC}
\newcolumntype{Y}{>{\centering\arraybackslash}X}
\usepackage[]{placeins}
\newcommand\extraspace{3pt}
\usepackage{placeins}
\usepackage{tikz}
\newcommand*\circled[1]{\tikz[baseline=(char.base)]{
            \node[shape=circle,draw,inner sep=0.8pt] (char) {#1};}}
\usepackage[framemethod=tikz]{mdframed}
\usepackage{afterpage}
\usepackage{stfloats}
\usepackage{atbegshi}
\newcommand{\handlethispage}{}
\newcommand{\discardpagesfromhere}{\let\handlethispage\AtBeginShipoutDiscard}
\newcommand{\keeppagesfromhere}{\let\handlethispage\relax}
\AtBeginShipout{\handlethispage}
\usepackage{comment}
\usepackage{float}
\usepackage{parskip}
\usepackage{amsmath}
\usepackage{multirow}
\usepackage[utf8]{inputenc}
\usepackage{fancyhdr}
\usepackage[title]{appendix}
\usepackage{wasysym}
\usepackage{url}
