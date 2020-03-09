#!/bin/bash

# ubuntu
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install python3.8
sudo apt-get install python3-pip 
sudo apt-get install texlive
sudo apt-get install git
sudo apt-get install dvipng texlive-latex-extra texlive-fonts-recommended 
rm pandoc*
wget "https://github.com/jgm/pandoc/releases/download/2.9.2/pandoc-2.9.2-1-amd64.deb"
sudo dpkg -i pandoc*
rm pandoc*


# macos
brew install git
brew install python3
brew install pandoc
brew install pandoc-citeproc

# pip packages
pip3 install --upgrade pip
pip3 install pandas
pip3 install pypandoc
pip3 install pandoc-eqnos