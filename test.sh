#!/bin/bash

#pylint  --output-format='html' $1.py > output.html
#run the pyhton script which should fill the pipeline with the sys exit code
python trial.py $1.py
rc=$?
if [[rc != 0]] then exit $rc;