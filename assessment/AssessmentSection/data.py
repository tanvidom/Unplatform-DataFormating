import json
import csv
import os
import glob
import re
#giving path to the folder where it will find all the json data files
os.chdir("./")
#Added a for loop to iterate over each json file in the directory to parse all the json files
for f in glob.glob("*.json"):
	filelist = f
	file = open(filelist)
	print f
	#	loaded the json file to the in python using the json module in python
#	file=open()
	data = json.load(file)
#creates a globla array
	mergedn=[]
#Appending the file name to the array
	mergedn.append(f)
#pulling required field from the json file one by one
	AssessmentTakenIDU = data["assessmentTakenId"]
	AssessmentTakenID = re.findall(r'%3A(.*?)%40',AssessmentTakenIDU,re.I)
	mergedn.append(AssessmentTakenID[0])
	AssessmentpartIDU = data["assessmentPartId"]
	AssessmentpartID = re.findall(r'%3A(.*?)%40',AssessmentpartIDU,re.I)
	mergedn.append(AssessmentpartID[0])
#creating/opening the csv file to which the python list(array) is to be written
#	mergedcsv = open('output.csv','a')
	mergedncsv = open('output-assessmentsection.csv','a')
#Added a for loop to iterate over a nested field in named "question" and pulled required field from it 
	for r in data ["questions"]:
		ItemIDU =r["itemId"]
		ItemID = re.findall(r'%3A(.*?)%40',ItemIDU,re.I)
		QuestionIDU =r["questionId"]
		QuestionID = re.findall(r'%3A(.*?)%40',QuestionIDU,re.I)
#Appended this required fieild to the array
		mergedn.append(ItemID[0])
		mergedn.append(QuestionID[0])						
#Added for loop to iterate over the response field in the json file
		for j in r["responses"]:
			ResponsesItemIDU=j["itemId"]
			ResponsesItemID = re.findall(r'%3A(.*?)%40',ResponsesItemIDU,re.I)
			mergedn.append(ResponsesItemID[0])
#added a if condition to skip or put null if the field is missing in the jsonfile
#			print j
			if 'missingResponse' not in j:
				if 'choiceIds' in j:
					choiceID=j["choiceIds"]
					mergedn.append(choiceID[0])
				elif 'text' in j:
					texttypeanswer=j["text"]["text"]
					mergedn.append(texttypeanswer)
			else:
				ResponsesMR=j["missingResponse"]		
				mergedn.append(ResponsesMR)
#print mergedn
#merged =[f,AssessmentTakenID,AssessmentpartID,ItemID,QuestionID,ResponsesMR,ResponsesItemID]
	writer = csv.writer(mergedncsv)
	writer.writerow(mergedn)