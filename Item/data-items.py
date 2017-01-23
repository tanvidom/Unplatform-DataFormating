import os
import json
import re
import csv
import glob
f = open('./58440994b3fcec051a40ea0c.json')

data1 = json.load(f)
list1=[]
# this variable is taking the question item id
questionITEMID = data1["question"]["itemId"]
# this variable is taking the the question_shuffle
SHUFFLE= data1["question"]["shuffle"]
list1.append(questionITEMID)
list1.append(SHUFFLE)
# this loop takes recordtypesids
for i in data1["recordTypeIds"]:
	QuestionRecordTypesID = i
	list1.append(QuestionRecordTypesID)
#this loop will take question_text_text
for c in data1["question"]["choices"]:
	for t in c["texts"]:
		#print t["text"]
		text1=t["text"]
		test=re.sub(r'<.*?>','',text1)
		print test
		for r in data1["answers"]:    
			ans=r["itemId"]
		#print ans
	