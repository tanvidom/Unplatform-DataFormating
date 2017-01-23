import os
import json
import re
import csv
import glob
f = open('./58440994b3fcec051a40ea0c.json')

data1 = json.load(f)
list1=[]
csv123 = open('output.csv','a')
# this variable is taking the question item id
questionITEMID = data1["question"]["itemId"]
# this variable is taking the the question_shuffle
SHUFFLE= data1["question"]["shuffle"]
list1.append(questionITEMID)
list1.append(SHUFFLE)
# this loop takes recordtypesids
for j in data1["question"]["texts"]:	
	questiontext=re.sub(r'<.*?>','',j["text"])
	list1.append(questiontext.encode('utf-8'))
for i in data1["question"]["recordTypeIds"]:
	QuestionRecordTypesID = i
	list1.append(QuestionRecordTypesID)	
#this loop will take question_text_text
for c in data1["question"]["choices"]:
	questionchoiceresponseid=c["id"]
	list1.append(questionchoiceresponseid)
	for t in c["texts"]:
		text1=t["text"]
		test=re.sub(r'<.*?>','',text1)
		list1.append(test.encode('utf-8'))		
writer = csv.writer(csv123)
writer.writerow(list1)		

#		for r in data1["answers"]:    
#			ans=r["itemId"]
#		print list1
#		