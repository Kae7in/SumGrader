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
pathToAllStudents = "/projects/cs439-norman/grading/_project0/students"

# Set this to the list of students to be graded
studentsToBeGraded = "eab3777_jmt3855/egp374_tjk922/eo4423_tn5523/etd349_ng8336/etg355_klt2399/fb5636_swj339/fc6877_mh46868/fl4424_ktv249/fm6532_ndn225/gm25639_mw33544/hc23277_mc57874/hcg359_mt32855/hck93_tz2853/hdv242_wc7923/hm22622_vr7336/ig3885_mjs5467/itc94_jc72462/jaz747_kks942/jbg2384_rbl498/jde2245_kd9357/jl48629_sl34978/jm68634_pak682/jm76685_vg5652/jma4436_vs8495/jtt767_tsn293/jwt925_oam397/"

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
