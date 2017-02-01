import os
import json
import re
import csv
import glob
import pdb
os.chdir("./")
for files in glob.glob("*.json"):
	file = files
	print file
	f=open(file)
#		f = open("58440994b3fcec051a40ea0c.json")
	list1=[]
	csv123 = open('output.csv','a')
	try:
		list1.append(file)
		data1 = json.load(f)
	except:
		print "error"	
# ------------ this portion looks for the question item id and if is shuffle or no --------------------------------	
	try:
		# this variable is taking the question item id
		questionITEMIDU = data1["question"]["itemId"]
		questionITEMID = re.findall(r'%3A(.*?)%40',questionITEMIDU,re.I)
		# this variable is taking the the question_shuffle
		SHUFFLE= data1["question"]["shuffle"]
		list1.append(questionITEMID[0])
		list1.append(SHUFFLE)		
	except:
		pass
#------------- this portion looks for the question text and its record type ------------------------------
	try:
		dict=data1["question"]
#this if condition and loop is added for checking if the question text feild exist and if exsist the loop through it and get the content and append it to the list
		if 'texts' in dict.keys():
			for j in data1["question"]["texts"]:	
				questiontext=re.sub(r'<.*?>','',j["text"])
				list1.append(questiontext.encode('utf-8'))
		else :
			list1.append("question text null")
		# this loop takes recordtypesids
		for i in data1["question"]["recordTypeIds"]:
			QuestionRecordTypesID = re.findall(r'%3A(.*?)%40',i,re.I)
			list1.append(QuestionRecordTypesID[0])	
	except:
		pass
#------------- This portion looks fot the choice response id and text and appents it to list1 ------------	
	try:
		if 'choices' in dict.keys():
			for c in data1["question"]["choices"]:
				questionchoiceresponseid=c["id"]
				list1.append(questionchoiceresponseid)
#				if "texts" in "choices":---not working--
				for t in c["texts"]:
					choices=t["text"]
					choicestext=re.sub(r'<.*?>','',choices)
					list1.append(choicestext.encode('utf-8'))
#				else:-----------not working----------
#					list1.append("null")
		else:
			list1.append("question choice response id null")
	except: 
		pass
#-----------------------------------------------------------------------------------------------------------

#------------ this portion takes the regex verions of question genus type ----------------------------------	
	try:
		if 'genusTypeId' in dict.keys():
				questiongenustypeId=data1["question"]["genusTypeId"]
				regenustypeid=re.findall(r'%3A(.*?)%40',questiongenustypeId,re.I)
				list1.append(regenustypeid[0])
		else:
			list1.append("question type genus id null")
	except:
		pass
#-----------------------------------------------------------------------------------------------------------	

#------------- this portion looks fo the display text of the activity name----------------------------------
	try:
		if 'displayName' in dict.keys():
			for a in data1["question"]["displayNames"]:
				Activityname=a["text"]
			list1.append(Activityname)
		else :
			list1.append("activity name null")
	except:
		pass
#-----------------------------------------------------------------------------------------------------------
#------------- This portion writes the csv file with the python list1---------------------------------------		
	writer =csv.writer(csv123)
	writer.writerow(list1)	
#------------------------------------------------------------------------------------------------------------	



#writer.writerow(["QuestionItenId","Shuffle","QuestionText","QuestionRecordTypeID","QuestionRecordTypeID","QuestionRecordTypeID","QuestionRecordTypeID","QuestionChoiceResponseId","QuestionChoiceText","QuestionChoiceResponseId","QuestionChoiceText","QuestionChoiceResponseId","QuestionChoiceText","QuestionChoiceResponseId","QuestionChoiceText","ActivityName"])

	#		for r in data1["answers"]:    
	#			ans=r["itemId"]
	#		print list1
	#		