import json
import csv
import os
import glob
#giving path to the folder where it will find all the json data files
os.chdir("./")
#Added a for loop to iterate over each json file in the directory to parse all the json files
#for f in glob.glob("*.json"):
#	filelist = f
#	file = open(filelist)
#	print f
#	loaded the json file to the in python using the json module in python
file=open("./5802203857e47513fc9e88ed.json")
data = json.load(file)
#	creates a globla array
mergedn=[]
#	Appending the file name to the array
mergedn.append(file)
#	pulling required field from the json file one by one
AssessmentTakenID = data["assessmentTakenId"]
mergedn.append(AssessmentTakenID)
AssessmentpartID = data["assessmentPartId"]	
mergedn.append(AssessmentpartID)
#	creating/opening the csv file to which the python list(array) is to be written
mergedcsv = open('output.csv','a')
mergedncsv = open('output1.csv','a')
#	Added a for loop to iterate over a nested field in named "question" and pulled required field from it 
for r in data ["questions"]:
	ItemID =r["itemId"]
	QuestionID =r["questionId"]
#		Appended this required fieild to the array
	mergedn.append(ItemID)
	mergedn.append(QuestionID)
#		Added for loop to iterate over the response field in the json file
	for j in r["responses"]:
		ResponsesItemID=j["itemId"]
#			added a if condition to skip or put null if the field is missing in the json file
		if 'missingResponse' not in j:
			ResponsesMR =  'null'
		else:
			ResponsesMR=j["missingResponse"]
#			Appended this required fields to the array
		mergedn.append(ResponsesItemID)
		mergedn.append(ResponsesMR)
#		print mergedn
#		merged =[f,AssessmentTakenID,AssessmentpartID,ItemID,QuestionID,ResponsesMR,ResponsesItemID]
writer = csv.writer(mergedncsv)
writer.writerow(mergedn)