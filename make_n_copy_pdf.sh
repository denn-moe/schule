#!/bin/bash

# i'm a noob, that's why...

make latexpdf
find ./build/latex -name "*.pdf" -exec cp {} ./pdf \;

SPHINXOPTS="-t loesung"
make latexpdf
find ./build/latex -name "*.pdf" -exec cp {} ./pdf/loesung \;

