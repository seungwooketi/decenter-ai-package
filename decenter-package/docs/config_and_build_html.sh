#!/bin/bash

target_dir=$(dirname $(pwd))
opt='-F -f -a --ext-autodoc -o '
opt2='--separate'
sphinx-apidoc $opt ./source/ $target_dir $opt2
#sphinx-apidoc $opt-F -f -a  —ext-autodoc -o ./source/ $target_diri 
make html
