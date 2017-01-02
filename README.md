# PyQuiz

	pyquiz.py
	~~~~~~~~~

	This is a quiz game that reads in any number of tab
	separated file(s) for its subject material.  It:
		1. Prompts the user for the Questions
		2. Test the response (exact match) to the answer

	Common file format is:
		question \t answer
	although reverse prompting can also be supplied:
		answer \t question

	Author:	Ray Lintner
	Date:	2016-12-12
	
	Version: 1.0

RUNNING THE QUIZ

To run the quiz, pass in the quiz data files are arguments to the program like the following:

$ python pyquiz.py 50states.dat 
$ python pyquiz.py hexidecimal.dat owasptopten.dat {etc...} 
