import json
import csv
import os
import glob
os.chdir("./assessment/AssessmentSection")
for f in glob.glob("*.json"):
	filelist = f
	file = open(filelist)
	#print f
	data = json.load(file)
	mergedn=[]
	mergedn.append(f)
	AssessmentTakenID = data["assessmentTakenId"]
	#print AssessmentTakenID
	mergedn.append(AssessmentTakenID)
	AssessmentpartID = data["assessmentPartId"]	
	#print AssessmentpartID
	mergedn.append(AssessmentpartID)
	mergedcsv = open('output.csv','a')
	mergedncsv = open('output1.csv','a')
	for r in data ["questions"]:
		ItemID =r["itemId"]
		QuestionID =r["questionId"]
		mergedn.append(ItemID)
		mergedn.append(QuestionID)
	#	print r
	 	for j in r["responses"]:
			ResponsesItemID=j["itemId"]
			if 'missingResponse' not in j:
				ResponsesMR = 'null'
			else:
				ResponsesMR=j["missingResponse"]
			mergedn.append(ResponsesItemID)
			mergedn.append(ResponsesMR)
	#		print ResponsesItemID
	#		print ResponsesMR
			merged =[f,AssessmentTakenID,AssessmentpartID,ItemID,QuestionID,ResponsesMR,ResponsesItemID]
	#		print len(merged)
			print len(mergedn)
	#		print merged
	#		print mergedn
	#		writer = csv.writer(mergedncsv)
	#		writer.writerow(mergedn)