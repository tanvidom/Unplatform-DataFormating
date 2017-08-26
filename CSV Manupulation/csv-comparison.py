import json
import csv
import os
import glob
import re
import pdb

#Function to open new json files in different folders, "array" parameter is passed to the function which contains question ID that is to be found in the assessment items folder.
def cdToItems(array):
	global itemsData
	os.chdir("/home/tdnshah/tools/Unplatform-DataFormating/Item")
	fileName = array
	print fileName
	fileExsist = os.path.isfile(fileName)
	print fileExsist
	if fileExsist == True:
		itemjsonFile = open(fileName)
		itemsData = json.load(itemjsonFile)		
	else:
		print "no file in the directory"
#Actual script starts from here 
#below changing to the directory in which Assessment Section json files are kept	
os.chdir("../assessment/AssessmentSection/")
dir_path1 = os.path.dirname(os.path.realpath(__file__))
print dir_path1
#pdb.set_trace()
print "loveu"
#for loop for ilterating through each assessmentsection json file in the directory
for files in glob.glob("*.json"):
	mergedcsv = open('test.csv','a')
	os.chdir(dir_path1)	
	dir_path2 = os.path.dirname(os.path.realpath(__file__))
	print dir_path2	
#	opens each json files
	file = open(files)
	print file
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
		SFquestionsItemIDU =questions["itemId"]
		SFquestionsItemID = re.findall(r'%3A(.*?)%40',SFquestionsItemIDU,re.I)
#		print str(questionsItemID).strip('[]')
		SFquestionsIDU =questions["questionId"]
		SFquestionsID = re.findall(r'%3A(.*?)%40',SFquestionsIDU,re.I)
		mainArray.append(SFquestionsID)
		print SFquestionsID
#---------------------------the scripts enters into the Items folder after this ------------	
		abc = SFquestionsID[0] + '.json'
#		print abc
		cdToItems(abc)
#		print itemsData
#		IFquestionITEMIDU = itemsData["question"]["itemId"]
#		IFquestionITEMID = re.findall(r'%3A(.*?)%40',IFquestionITEMIDU,re.I)#--------to be added

		try:
			dict=itemsData["question"] 
			if 'texts' in dict.keys():
				for j in itemsData["question"]["texts"]:	
					questiontext=re.sub(r'<.*?>','',j["text"])
#					print questiontext
					mainArray.append(questiontext.encode('utf-8'))#------to be added
			elif 'text' in dict.keys():
				QTinlinechoice = itemsData["question"]["text"]["text"]
				mainArray.append(re.sub(r'<.*?>','',QTinlinechoice))#-----------to be added
#				print QTinlinechoice
			else :
#				print "Question text is null"
				mainArray.append("question text null")#--------------to be added
#	 			this loop takes recordtypesids
#				for i in itemsData["question"]["recordTypeIds"]:
#					QuestionRecordTypesID = re.findall(r'%3A(.*?)%40',i,re.I)
#				print QuestionRecordTypesID
#				list1.append(QuestionRecordTypesID[0])	------------to be added
		except:
				print "error level 1"
		try:
			if 'choices' in dict.keys():
				for c in itemsData["question"]["choices"]:
					questionchoiceresponseid=c["id"]
#					print questionchoiceresponseid
					mainArray.append(questionchoiceresponseid)
	#				if "texts" in "choices":
					for t in c["texts"]:
						choices=t["text"]
						choicestext=re.sub(r'<.*?>','',choices)
#						print choicestext
						mainArray.append(choicestext.encode('utf-8'))
#						print mainArray
	#				else:
	#					print "lowed"
#						mainArray.append("null")				
			else:
				print "didnt found choices"
#				mainArray.append("question choice response id null")
		except:
			print "tried but found choices"
			pass
#		mergedncsv = open('output1.csv','a')
	writer = csv.writer(mergedcsv)
	writer.writerow(mainArray)
