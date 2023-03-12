#!/bin/bash

# i'm a noob, that's why...

make latexpdf
find ./build/latex -name "*.pdf" -exec cp {} ./pdf \;

make SPHINXOPTS="-t loesung" latexpdf
find ./build/latex -name "*.pdf" -exec cp {} ./pdf/loesung \;

make html SPHINXOPTS="-t loesung"
