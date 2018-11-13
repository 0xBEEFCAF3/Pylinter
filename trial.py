# -*- coding: utf-8 -*-

__author__ = "ArminSabouri"

from pylint.lint import Run
import sys
import os
import re
from pylint import epylint as lint

#Class contains basic colors that can be displayed in terminal window
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def test_platform(path):
	#dictionary to to collect filenames with the ocrrenspoding number of errors and warnings
	f = {}

	for root, dirs, files in os.walk(".", topdown=False):
		for name in files:
			try:
				x = name.split(".")
			except Exception, e:
				sys.stdout.write(e)
				sys.exit(100)
			
			if x[1] == 'py':
				print(bcolors.HEADER + str(name) + bcolors.ENDC)
				result = lint(name)
				sys.stdout.write(result[0])
				if not result[1]:
					#Error or Warning detected by PyLint
					#Add to dict ==> 'File_name' : 'Warnings'
					f[os.path.join(root, name)] = ("Errors: " + str(result[2]), "Warnings: "  + str(result[3]))
	print(f)


def lint(file_name):
	results = Run(['-rn', file_name], exit=False)
	#(pylint_stdout, pylint_stderr) = lint.py_run(file_name, return_std=True)
	
	#print("Global Score:" , results.linter.stats['global_note'])
	print("Warnings:" , results.linter.stats['warning'])
	print("Errors: " , results.linter.stats['error'])

	errors = results.linter.stats['error']
	warnings = results.linter.stats['warning']

	if errors >= 1 or warnings >= 1 : return [bcolors.FAIL + 
	"Python file does not meet minimum requirments. Fix before commit!\n " + bcolors.ENDC
	,False,errors,warnings]
	return (bcolors.OKBLUE + "Commit going through\n " + bcolors.ENDC,True)


if __name__ == "__main__":


	#example of how you would test lint
	"""
	result = lint(sys.argv[1])
	sys.stdout.write(result[0])
	if result[1]: sys.exit(0)
	else: sys.exit(100)
	"""


	#Test the whole platform
	test_platform(".")
