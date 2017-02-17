

import json
import csv
import os
import glob
import re
import pdb

def cdToItems(array):
	global itemsData
	os.chdir("/home/tdnshah/Unplatform-DataFormating/Item")
	fileName = array
#	print fileName
	fileExsist = os.path.isfile(fileName)
	print fileExsist
	if fileExsist == True:
		itemjsonFile = open(fileName)
		itemsData = json.load(itemjsonFile)		
	else:
		print "no file in the directory"
	
os.chdir("../assessment/AssessmentSection/")
dir_path1 = os.path.dirname(os.path.realpath(__file__))
print dir_path1
#pdb.set_trace()
print "loveu"
#for loop for ilterating through each assessmentsection json file in the directory
for files in glob.glob("*.json"):
	os.chdir("/home/tdnshah/Unplatform-DataFormating/assessment/AssessmentSection/")	
	dir_path2 = os.path.dirname(os.path.realpath(__file__))
	print dir_path2	
#	opens each json files
	file = open(files)
#	loads a file to json module
	data = json.load(file)	
#	declared a global array
	mainArray = []
#	file name appended to the array
	mainArray.append(files)
#getting the assessmenttakenids and assessmentpartids
	AssessmentTakenIDU = data["assessmentTakenId"]
	AssessmentTakenID = re.findall(r'%3A(.*?)%40',AssessmentTakenIDU,re.I)
	AssessmentpartIDU = data["assessmentPartId"]
	AssessmentpartID = re.findall(r'%3A(.*?)%40',AssessmentpartIDU,re.I)
	mainArray.append(AssessmentTakenID)
	mainArray.append(AssessmentpartID)
	for questions in data ["questions"]:
		questionsItemIDU =questions["itemId"]
		questionsItemID = re.findall(r'%3A(.*?)%40',questionsItemIDU,re.I)
		print str(questionsItemID).strip('[]')
		questionsIDU =questions["questionId"]
		questionsID = re.findall(r'%3A(.*?)%40',questionsIDU,re.I)
#		print os.getcwd()
#		os.chdir("/home/tdnshah/Unplatform-DataFormating/Item")
#		dir_path3 = os.path.dirname(os.path.realpath(__file__))
#		print dir_path3	 
#		 = questionsID[0]
#		cd = abc + ".json"
#		print os.path.isfile(cd)
		abc = questionsID[0] + '.json'
		print abc
		cdToItems(abc)
		abc = itemsData["recordTypeIds"]
		print abc
				  

		
		
				
		
		
		

	
		