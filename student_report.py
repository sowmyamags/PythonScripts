#!/usr/lib/env python3

def student_grade(name, grade):
	result = "{} received {}%  on the exam".format(name,grade)
	if name and grade == True:
		return result
	elif name == True:
		return "No grade given"
	elif grade == True:
		return "No Name given"
	else:
		return "No details given"
