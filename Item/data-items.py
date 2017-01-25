import os
import json
import re
import csv
import glob
os.chdir("./")
for files in glob.glob("*.json"):
	file = files
	print file
	f=open(file)
#		f = open("58440994b3fcec051a40ea0c.json")
	try:
		data1 = json.load(f)
	except:
		pass
	list1=[]
	list1.append(file)
	csv123 = open('output.csv','a')
	try:
		# this variable is taking the question item id
		questionITEMID = data1["question"]["itemId"]
		# this variable is taking the the question_shuffle
		SHUFFLE= data1["question"]["shuffle"]
		list1.append(questionITEMID)
		list1.append(SHUFFLE)
		#this if condition and loop is added for checking if the question text feild exist and if exsist the loop through it and get the content and append it to the list
	except:
		pass
	try:
		dict=data1["question"]
		if 'texts' in dict.keys():
			for j in data1["question"]["texts"]:	
				questiontext=re.sub(r'<.*?>','',j["text"])
				list1.append(questiontext.encode('utf-8'))
		else :
			list1.append("null")
		# this loop takes recordtypesids
		for i in data1["question"]["recordTypeIds"]:
			QuestionRecordTypesID = i
			list1.append(QuestionRecordTypesID)	
		#this loop will take question_text_text_forchoices
	except:
		pass
	try:
		if 'choices' in dict.keys():
			for c in data1["question"]["choices"]:
				questionchoiceresponseid=c["id"]
				list1.append(questionchoiceresponseid)
#				if "texts" in "choices":
				for t in c["texts"]:
					text1=t["text"]
					test=re.sub(r'<.*?>','',text1)
					list1.append(test.encode('utf-8'))
#				else:
#					list1.append("null")
	except: 
		pass
	else:
		list1.append("null")
	try:
		if 'displayNames' in dict.keys():
			for a in data1["question"]["displayNames"]:
				Activityname=a["text"]
			list1.append(Activityname)
		else :
			list1.append("null")
		writer =csv.writer(csv123)
		writer.writerow(list1)
	except:
		pass

#writer.writerow(["QuestionItenId","Shuffle","QuestionText","QuestionRecordTypeID","QuestionRecordTypeID","QuestionRecordTypeID","QuestionRecordTypeID","QuestionChoiceResponseId","QuestionChoiceText","QuestionChoiceResponseId","QuestionChoiceText","QuestionChoiceResponseId","QuestionChoiceText","QuestionChoiceResponseId","QuestionChoiceText","ActivityName"])

	#		for r in data1["answers"]:    
	#			ans=r["itemId"]
	#		print list1
	#		