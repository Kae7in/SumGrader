import os
import re
import linecache


"""
SUM GRADER

This Python script traverses all student directories, scavenging for their
feedback.txt files, and sums the design and documentation grades in each of them.
The result is an output pairing each student's eid with their overall grade. This
helps avoid having to do hand calculations.
"""


###############################################################
# Set this to the path of all student directories
pathToAllStudents = "/absolute/path/to/students/..."

# Set this to the list of students to be graded
studentsToBeGraded = "exampleEID1_exampleEID2/exampleEID3_exampleEID4/.../"

# Set the line numbers (0-indexed) of the feedback.txt file with the actual scores to sum
gradeLines = [0, 2, 6, 7, 9, 10, 11, 13, 16, 17]
###############################################################

regexResult = re.findall(r'[a-z]+[0-9]+', studentsToBeGraded)
studentGrades = {}
for eid in regexResult:
	#open student's feedback.txt file
	feedbackPath = pathToAllStudents + '/' + eid + '/feedback.txt'
	try:
		feedbackFile = open(feedbackPath)
		try:
			feedbackLines = feedbackFile.readlines()
		finally:
			feedbackFile.close()
	except IOError:
		print("Warning: can\'t find file for path: " + feedbackPath)
		continue

	# sum grades
	gradeTotal = 0
	for num in gradeLines:
		line = feedbackLines[num]
		line = line.split(':')[-1]
		if not line:
			continue

		# this robust regex line protects against weird typos or spacing errors
		# it only grabs the last integer on the line specified (the specified grade)
		grade = re.match(r'^(.*?)(\d+)(\D*)$', line)
		if not grade:
			continue
		gradeTotal += int(grade.group(2))
		
	# place in dictionary
	studentGrades[eid] = gradeTotal

if studentGrades:
        for student, grade in studentGrades.iteritems():
                print(student + " " + str(grade))
