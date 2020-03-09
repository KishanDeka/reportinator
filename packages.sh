#!/bin/bash

# ubuntu
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install python3
sudo apt-get install git
rm pandoc*
wget "https://github.com/jgm/pandoc/releases/download/2.9.2/pandoc-2.9.2-1-amd64.deb"
sudo dpkg -i pandoc*
rm pandoc*
sudo apt-get install texlive

# macos
brew install git
brew install python3
brew install pandoc
brew install pandoc-citeproc

# pip packages
pip3 install --upgrade pip
pip3 install pypandoc
pip3 install pandoc-eqnos