"""
	pyquiz.py
	~~~~~~~~~

	This is a quiz game that reads in any number of tab
	separated file(s) for its subject material.  It:
		1. Prompts the user for the Questions
		2. Tests the response (exact match) to the answer

	Common file format is:
		question \t answer
	although reverse prompting can also be supplied:
		answer \t question

	Author:	Ray Lintner
	Date:	2016-12-12
	
	Version: 1.0 - Initial
	Version: 2.0 - Added repeat for incorrect answers
"""

import sys
import random

lines=[]

## check inputfiles were passed in args
if len(sys.argv) < 2 :
	print "YOU MUST PASS AT LEAST ONE INPUT FILE TO THIS PROGRAM...EXITING..."
	exit()
else :
	## process input files; bypass argv[0]
	for file in sys.argv[1:] :
		# read file into list
		with open(file) as f:
			fdata = f.readlines()
		# read list into lines
		for line in fdata:
			lines.append(line)
	
	# get number of lines / size of data
	len_lines = len(lines)

	incorrect = False
	# Play Quiz
	while True:
		if incorrect == False :
			# gen a random line number from data set
			random_num = random.randrange(0,len_lines)
		
			# split line by tab into Q&A
			split_line = lines[random_num].split("\t");
			question = split_line[0]
			answer = split_line[1]
		
		# prompt and test
		print ""
		print question
		response = sys.stdin.readline()
		#response = response.rstrip('\n')
		if (response == answer):
			print "CORRECT!"
			incorrect = False
		else:
			print "WRONG, the answer is: %s" %answer
			incorrect = True
				

	

		


