from sets import Set
from math import log
import re
import numpy as np
import matplotlib as plt 
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.neural_network import MLPClassifier
trainTopics = [] #lisdyt of list of topics, "None"  if no topic
trainTitle = []
trainBody = []

testTopics = [] #lisdyt of list of topics, "None"  if no topic
testTitle = []
testBody = []
termFrequency = list(dict())
with open("reuters/reut2-000.sgm") as f:
    content = f.readlines()

content = [x.strip() for x in content] 

i=1
while i < range(len(content)):
	linesplit = content[i].split(" ")
	if "<REUTERS" in linesplit:
		print i
		if "TOPICS=\"NO\"" in linesplit:
			i+=1
			continue
		isBodyPresent = False
		isTitlePresent = False
		if "LEWISSPLIT=\"TRAIN\"" in linesplit:
			

			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					trainTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						trainTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						trainTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					trainBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				trainBody.append(" ")
			if isTitlePresent == False:
				trainTitle.append(" ")
			


		elif "LEWISSPLIT=\"TEST\"" in linesplit:
			isBodyPresent = False
			isTitlePresent = False			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					testTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						testTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						testTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					testBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				testBody.append(" ")
			if isTitlePresent == False:
				testTitle.append(" ")
	else:
		i+=1
	if i >= len(content):
		break
with open("reuters/reut2-001.sgm") as f:
    content = f.readlines()

content = [x.strip() for x in content] 
1
i=1
while i < range(len(content)):
	linesplit = content[i].split(" ")
	if "<REUTERS" in linesplit:
		if "TOPICS=\"NO\"" in linesplit:
			i+=1
			continue
		isBodyPresent = False
		isTitlePresent = False
		if "LEWISSPLIT=\"TRAIN\"" in linesplit:
			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					trainTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						trainTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						trainTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					trainBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				trainBody.append(" ")
			if isTitlePresent == False:
				trainTitle.append(" ")
			


		elif "LEWISSPLIT=\"TEST\"" in linesplit:
			isBodyPresent = False
			isTitlePresent = False			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					testTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						testTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						testTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					testBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				testBody.append(" ")
			if isTitlePresent == False:
				testTitle.append(" ")
	else:
		i+=1
	if i >= len(content):
		break

with open("reuters/reut2-002.sgm") as f:
    content = f.readlines()

content = [x.strip() for x in content] 

i=1
while i < range(len(content)):
	linesplit = content[i].split(" ")
	if "<REUTERS" in linesplit:
		if "TOPICS=\"NO\"" in linesplit:
			i+=1
			continue
		isBodyPresent = False
		isTitlePresent = False
		if "LEWISSPLIT=\"TRAIN\"" in linesplit:
			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					trainTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						trainTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						trainTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					trainBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				trainBody.append(" ")
			if isTitlePresent == False:
				trainTitle.append(" ")
			


		elif "LEWISSPLIT=\"TEST\"" in linesplit:
			isBodyPresent = False
			isTitlePresent = False			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					testTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						testTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						testTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					testBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				testBody.append(" ")
			if isTitlePresent == False:
				testTitle.append(" ")
	else:
		i+=1
	if i >= len(content):
		break		
with open("reuters/reut2-003.sgm") as f:
    content = f.readlines()

content = [x.strip() for x in content] 

i=1
while i < range(len(content)):
	linesplit = content[i].split(" ")
	if "<REUTERS" in linesplit:
		if "TOPICS=\"NO\"" in linesplit:
			i+=1
			continue
		isBodyPresent = False
		isTitlePresent = False
		if "LEWISSPLIT=\"TRAIN\"" in linesplit:
			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					trainTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						trainTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						trainTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					trainBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				trainBody.append(" ")
			if isTitlePresent == False:
				trainTitle.append(" ")
			


		elif "LEWISSPLIT=\"TEST\"" in linesplit:
			isBodyPresent = False
			isTitlePresent = False			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					testTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						testTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						testTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					testBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				testBody.append(" ")
			if isTitlePresent == False:
				testTitle.append(" ")
	else:
		i+=1
	if i >= len(content):
		break

with open("reuters/reut2-004.sgm") as f:
    content = f.readlines()

content = [x.strip() for x in content] 

i=1
while i < range(len(content)):
	linesplit = content[i].split(" ")
	if "<REUTERS" in linesplit:
		if "TOPICS=\"NO\"" in linesplit:
			i+=1
			continue
		isBodyPresent = False
		isTitlePresent = False
		if "LEWISSPLIT=\"TRAIN\"" in linesplit:
			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					trainTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						trainTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						trainTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					trainBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				trainBody.append(" ")
			if isTitlePresent == False:
				trainTitle.append(" ")
			


		elif "LEWISSPLIT=\"TEST\"" in linesplit:
			isBodyPresent = False
			isTitlePresent = False			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					testTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						testTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						testTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					testBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				testBody.append(" ")
			if isTitlePresent == False:
				testTitle.append(" ")
	else:
		i+=1
	if i >= len(content):
		break

with open("reuters/reut2-005.sgm") as f:
    content = f.readlines()

content = [x.strip() for x in content] 

i=1
while i < range(len(content)):
	linesplit = content[i].split(" ")
	if "<REUTERS" in linesplit:
		if "TOPICS=\"NO\"" in linesplit:
			i+=1
			continue
		isBodyPresent = False
		isTitlePresent = False
		if "LEWISSPLIT=\"TRAIN\"" in linesplit:
			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					trainTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						trainTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						trainTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					trainBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				trainBody.append(" ")
			if isTitlePresent == False:
				trainTitle.append(" ")
			


		elif "LEWISSPLIT=\"TEST\"" in linesplit:
			isBodyPresent = False
			isTitlePresent = False			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					testTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						testTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						testTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					testBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				testBody.append(" ")
			if isTitlePresent == False:
				testTitle.append(" ")
	else:
		i+=1
	if i >= len(content):
		break

with open("reuters/reut2-006.sgm") as f:
    content = f.readlines()

content = [x.strip() for x in content] 

i=1
while i < range(len(content)):
	linesplit = content[i].split(" ")
	if "<REUTERS" in linesplit:
		if "TOPICS=\"NO\"" in linesplit:
			i+=1
			continue
		isBodyPresent = False
		isTitlePresent = False
		if "LEWISSPLIT=\"TRAIN\"" in linesplit:
			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					trainTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						trainTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						trainTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					trainBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				trainBody.append(" ")
			if isTitlePresent == False:
				trainTitle.append(" ")
			


		elif "LEWISSPLIT=\"TEST\"" in linesplit:
			isBodyPresent = False
			isTitlePresent = False			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					testTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						testTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						testTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					testBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				testBody.append(" ")
			if isTitlePresent == False:
				testTitle.append(" ")
	else:
		i+=1
	if i >= len(content):
		break

with open("reuters/reut2-007.sgm") as f:
    content = f.readlines()

content = [x.strip() for x in content] 

i=1
while i < range(len(content)):
	linesplit = content[i].split(" ")
	if "<REUTERS" in linesplit:
		if "TOPICS=\"NO\"" in linesplit:
			i+=1
			continue
		isBodyPresent = False
		isTitlePresent = False
		if "LEWISSPLIT=\"TRAIN\"" in linesplit:
			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					trainTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						trainTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						trainTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					trainBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				trainBody.append(" ")
			if isTitlePresent == False:
				trainTitle.append(" ")
			


		elif "LEWISSPLIT=\"TEST\"" in linesplit:
			isBodyPresent = False
			isTitlePresent = False			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					testTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						testTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						testTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					testBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				testBody.append(" ")
			if isTitlePresent == False:
				testTitle.append(" ")
	else:
		i+=1
	if i >= len(content):
		break

with open("reuters/reut2-008.sgm") as f:
    content = f.readlines()

content = [x.strip() for x in content] 

i=1
while i < range(len(content)):
	linesplit = content[i].split(" ")
	if "<REUTERS" in linesplit:
		if "TOPICS=\"NO\"" in linesplit:
			i+=1
			continue
		isBodyPresent = False
		isTitlePresent = False
		if "LEWISSPLIT=\"TRAIN\"" in linesplit:
			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					trainTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						trainTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						trainTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					trainBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				trainBody.append(" ")
			if isTitlePresent == False:
				trainTitle.append(" ")
			


		elif "LEWISSPLIT=\"TEST\"" in linesplit:
			isBodyPresent = False
			isTitlePresent = False			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					testTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						testTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						testTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					testBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				testBody.append(" ")
			if isTitlePresent == False:
				testTitle.append(" ")
	else:
		i+=1
	if i >= len(content):
		break

with open("reuters/reut2-009.sgm") as f:
    content = f.readlines()

content = [x.strip() for x in content] 

i=1
while i < range(len(content)):
	linesplit = content[i].split(" ")
	if "<REUTERS" in linesplit:
		if "TOPICS=\"NO\"" in linesplit:
			i+=1
			continue
		isBodyPresent = False
		isTitlePresent = False
		if "LEWISSPLIT=\"TRAIN\"" in linesplit:
			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					trainTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						trainTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						trainTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					trainBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				trainBody.append(" ")
			if isTitlePresent == False:
				trainTitle.append(" ")
			


		elif "LEWISSPLIT=\"TEST\"" in linesplit:
			isBodyPresent = False
			isTitlePresent = False			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					testTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						testTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						testTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					testBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				testBody.append(" ")
			if isTitlePresent == False:
				testTitle.append(" ")
	else:
		i+=1
	if i >= len(content):
		break

with open("reuters/reut2-010.sgm") as f:
    content = f.readlines()

content = [x.strip() for x in content] 

i=1
while i < range(len(content)):
	linesplit = content[i].split(" ")
	if "<REUTERS" in linesplit:
		if "TOPICS=\"NO\"" in linesplit:
			i+=1
			continue
		isBodyPresent = False
		isTitlePresent = False
		if "LEWISSPLIT=\"TRAIN\"" in linesplit:
			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					trainTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						trainTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						trainTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					trainBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				trainBody.append(" ")
			if isTitlePresent == False:
				trainTitle.append(" ")
			


		elif "LEWISSPLIT=\"TEST\"" in linesplit:
			isBodyPresent = False
			isTitlePresent = False			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					testTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						testTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						testTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					testBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				testBody.append(" ")
			if isTitlePresent == False:
				testTitle.append(" ")
	else:
		i+=1
	if i >= len(content):
		break

with open("reuters/reut2-011.sgm") as f:
    content = f.readlines()

content = [x.strip() for x in content] 

i=1
while i < range(len(content)):
	linesplit = content[i].split(" ")
	if "<REUTERS" in linesplit:
		if "TOPICS=\"NO\"" in linesplit:
			i+=1
			continue
		isBodyPresent = False
		isTitlePresent = False
		if "LEWISSPLIT=\"TRAIN\"" in linesplit:
			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					trainTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						trainTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						trainTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					trainBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				trainBody.append(" ")
			if isTitlePresent == False:
				trainTitle.append(" ")
			


		elif "LEWISSPLIT=\"TEST\"" in linesplit:
			isBodyPresent = False
			isTitlePresent = False			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					testTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						testTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						testTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					testBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				testBody.append(" ")
			if isTitlePresent == False:
				testTitle.append(" ")
	else:
		i+=1
	if i >= len(content):
		break

with open("reuters/reut2-012.sgm") as f:
    content = f.readlines()

content = [x.strip() for x in content] 

i=1
while i < range(len(content)):
	linesplit = content[i].split(" ")
	if "<REUTERS" in linesplit:
		if "TOPICS=\"NO\"" in linesplit:
			i+=1
			continue
		if "LEWISSPLIT=\"NOT-USED\"" in linesplit:
			i+=1
			continue
		isBodyPresent = False
		isTitlePresent = False
		if "LEWISSPLIT=\"TRAIN\"" in linesplit:
			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					trainTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						trainTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						trainTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					trainBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				trainBody.append(" ")
			if isTitlePresent == False:
				trainTitle.append(" ")
			


		elif "LEWISSPLIT=\"TEST\"" in linesplit:
			isBodyPresent = False
			isTitlePresent = False			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					testTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						testTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						testTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					testBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				testBody.append(" ")
			if isTitlePresent == False:
				testTitle.append(" ")
	else:
		i+=1
	if i >= len(content):
		break

with open("reuters/reut2-013.sgm") as f:
    content = f.readlines()

content = [x.strip() for x in content] 

i=1
while i < range(len(content)):
	linesplit = content[i].split(" ")
	if "<REUTERS" in linesplit:
		if "TOPICS=\"NO\"" in linesplit:
			i+=1
			continue
		if "LEWISSPLIT=\"NOT-USED\"" in linesplit:
			i+=1
			continue
		
		isBodyPresent = False
		isTitlePresent = False
		if "LEWISSPLIT=\"TRAIN\"" in linesplit:
			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					trainTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						trainTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						trainTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					trainBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				trainBody.append(" ")
			if isTitlePresent == False:
				trainTitle.append(" ")
			


		elif "LEWISSPLIT=\"TEST\"" in linesplit:
			isBodyPresent = False
			isTitlePresent = False			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					testTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						testTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						testTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					testBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				testBody.append(" ")
			if isTitlePresent == False:
				testTitle.append(" ")
	else:
		i+=1
	if i >= len(content):
		break

with open("reuters/reut2-014.sgm") as f:
    content = f.readlines()

content = [x.strip() for x in content] 

i=1
while i < range(len(content)):
	linesplit = content[i].split(" ")
	if "<REUTERS" in linesplit:
		if "TOPICS=\"NO\"" in linesplit:
			i+=1
			continue
		if "LEWISSPLIT=\"NOT-USED\"" in linesplit:
			i+=1
			continue
		
		isBodyPresent = False
		isTitlePresent = False
		if "LEWISSPLIT=\"TRAIN\"" in linesplit:
			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					trainTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						trainTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						trainTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					trainBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				trainBody.append(" ")
			if isTitlePresent == False:
				trainTitle.append(" ")
			


		elif "LEWISSPLIT=\"TEST\"" in linesplit:
			isBodyPresent = False
			isTitlePresent = False			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					testTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						testTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						testTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					testBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				testBody.append(" ")
			if isTitlePresent == False:
				testTitle.append(" ")
	else:
		i+=1
	if i >= len(content):
		break

with open("reuters/reut2-015.sgm") as f:
    content = f.readlines()

content = [x.strip() for x in content] 

i=1
while i < range(len(content)):
	linesplit = content[i].split(" ")
	if "<REUTERS" in linesplit:
		if "TOPICS=\"NO\"" in linesplit:
			i+=1
			continue
		if "LEWISSPLIT=\"NOT-USED\"" in linesplit:
			i+=1
			continue
		
		isBodyPresent = False
		isTitlePresent = False
		if "LEWISSPLIT=\"TRAIN\"" in linesplit:
			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					trainTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						trainTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						trainTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					trainBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				trainBody.append(" ")
			if isTitlePresent == False:
				trainTitle.append(" ")
			


		elif "LEWISSPLIT=\"TEST\"" in linesplit:
			isBodyPresent = False
			isTitlePresent = False			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					testTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						testTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						testTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					testBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				testBody.append(" ")
			if isTitlePresent == False:
				testTitle.append(" ")
	else:
		i+=1
	if i >= len(content):
		break

with open("reuters/reut2-016.sgm") as f:
    content = f.readlines()

content = [x.strip() for x in content] 

i=1
while i < range(len(content)):
	linesplit = content[i].split(" ")
	if "<REUTERS" in linesplit:
		if "TOPICS=\"NO\"" in linesplit:
			i+=1
			continue
		if "LEWISSPLIT=\"NOT-USED\"" in linesplit:
			i+=1
			continue
		
		isBodyPresent = False
		isTitlePresent = False
		if "LEWISSPLIT=\"TRAIN\"" in linesplit:
			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					trainTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						trainTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						trainTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					trainBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				trainBody.append(" ")
			if isTitlePresent == False:
				trainTitle.append(" ")
			


		elif "LEWISSPLIT=\"TEST\"" in linesplit:
			isBodyPresent = False
			isTitlePresent = False			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					testTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						testTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						testTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					testBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				testBody.append(" ")
			if isTitlePresent == False:
				testTitle.append(" ")
	else:
		i+=1
	if i >= len(content):
		break

with open("reuters/reut2-017.sgm") as f:
    content = f.readlines()

content = [x.strip() for x in content] 

i=1
while i < range(len(content)):
	linesplit = content[i].split(" ")
	if "<REUTERS" in linesplit:
		if "TOPICS=\"NO\"" in linesplit:
			i+=1
			continue
		if "LEWISSPLIT=\"NOT-USED\"" in linesplit:
			i+=1
			continue
		
		isBodyPresent = False
		isTitlePresent = False
		if "LEWISSPLIT=\"TRAIN\"" in linesplit:
			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					trainTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						trainTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						trainTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					trainBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				trainBody.append(" ")
			if isTitlePresent == False:
				trainTitle.append(" ")
			


		elif "LEWISSPLIT=\"TEST\"" in linesplit:
			isBodyPresent = False
			isTitlePresent = False			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					testTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						testTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						testTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					testBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				testBody.append(" ")
			if isTitlePresent == False:
				testTitle.append(" ")
	else:
		i+=1
	if i >= len(content):
		break

with open("reuters/reut2-018.sgm") as f:
    content = f.readlines()

content = [x.strip() for x in content] 

i=1
while i < range(len(content)):
	linesplit = content[i].split(" ")
	if "<REUTERS" in linesplit:
		if "TOPICS=\"NO\"" in linesplit:
			i+=1
			continue
		if "LEWISSPLIT=\"NOT-USED\"" in linesplit:
			i+=1
			continue
		
		isBodyPresent = False
		isTitlePresent = False
		if "LEWISSPLIT=\"TRAIN\"" in linesplit:
			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					trainTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						trainTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						trainTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					trainBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				trainBody.append(" ")
			if isTitlePresent == False:
				trainTitle.append(" ")
			


		elif "LEWISSPLIT=\"TEST\"" in linesplit:
			isBodyPresent = False
			isTitlePresent = False			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					testTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						testTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						testTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					testBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				testBody.append(" ")
			if isTitlePresent == False:
				testTitle.append(" ")
	else:
		i+=1
	if i >= len(content):
		break

with open("reuters/reut2-019.sgm") as f:
    content = f.readlines()

content = [x.strip() for x in content] 

i=1
while i < range(len(content)):
	linesplit = content[i].split(" ")
	if "<REUTERS" in linesplit:
		if "TOPICS=\"NO\"" in linesplit:
			i+=1
			continue
		if "LEWISSPLIT=\"NOT-USED\"" in linesplit:
			i+=1
			continue
		
		isBodyPresent = False
		isTitlePresent = False
		if "LEWISSPLIT=\"TRAIN\"" in linesplit:
			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					trainTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						trainTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						trainTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					trainBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				trainBody.append(" ")
			if isTitlePresent == False:
				trainTitle.append(" ")
			


		elif "LEWISSPLIT=\"TEST\"" in linesplit:
			isBodyPresent = False
			isTitlePresent = False			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					testTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						testTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						testTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					testBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				testBody.append(" ")
			if isTitlePresent == False:
				testTitle.append(" ")
	else:
		i+=1
	if i >= len(content):
		break

with open("reuters/reut2-020.sgm") as f:
    content = f.readlines()

content = [x.strip() for x in content] 

i=1
while i < range(len(content)):
	linesplit = content[i].split(" ")
	if "<REUTERS" in linesplit:
		if "TOPICS=\"NO\"" in linesplit:
			i+=1
			continue
		if "LEWISSPLIT=\"NOT-USED\"" in linesplit:
			i+=1
			continue
		
		isBodyPresent = False
		isTitlePresent = False
		if "LEWISSPLIT=\"TRAIN\"" in linesplit:
			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					trainTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						trainTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						trainTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					trainBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				trainBody.append(" ")
			if isTitlePresent == False:
				trainTitle.append(" ")
			


		elif "LEWISSPLIT=\"TEST\"" in linesplit:
			isBodyPresent = False
			isTitlePresent = False			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					testTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						testTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						testTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					testBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				testBody.append(" ")
			if isTitlePresent == False:
				testTitle.append(" ")
	else:
		i+=1
	if i >= len(content):
		break

with open("reuters/reut2-021.sgm") as f:
    content = f.readlines()

content = [x.strip() for x in content] 

i=1
while i < range(len(content)):
	linesplit = content[i].split(" ")
	if "<REUTERS" in linesplit:
		if "TOPICS=\"NO\"" in linesplit:
			i+=1
			continue
		if "LEWISSPLIT=\"NOT-USED\"" in linesplit:
			i+=1
			continue
		
		isBodyPresent = False
		isTitlePresent = False
		if "LEWISSPLIT=\"TRAIN\"" in linesplit:
			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					trainTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						trainTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						trainTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					trainBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				trainBody.append(" ")
			if isTitlePresent == False:
				trainTitle.append(" ")
			


		elif "LEWISSPLIT=\"TEST\"" in linesplit:
			isBodyPresent = False
			isTitlePresent = False			
			while content[i+1]!="</REUTERS>":
				if content[i].startswith('<TITLE>'):
					titleSplit = content[i].split("<TITLE>")
					titleSplitx = titleSplit[1].split("</TITLE>")
					isTitlePresent = True
					testTitle.append(titleSplitx[0])
				if content[i].startswith('<TOPICS>'):
					splitTopics = content[i].split("<D>")
					if len(splitTopics) == 1:
						testTopics.append(["None"])
					else:
						topicX = []
						for j in range(len(splitTopics)):
							if j == 0:
								continue
							splitX = splitTopics[j].split("</D>")
							topicX.append(splitX[0])
						testTopics.append(topicX)
				xsplit = content[i].split("</DATELINE><BODY>")
				if len(xsplit) == 2:
					body = xsplit[1]
					i=i+1
					while content[i+1] != "&#3;</BODY></TEXT>":
						body = body + " " + content[i]
						i = i+1
					testBody.append(body)
					isBodyPresent = True
					continue
				i = i+1
				if  i >= len(content):
					break
			if isBodyPresent == False:
				testBody.append(" ")
			if isTitlePresent == False:
				testTitle.append(" ")
	else:
		i+=1
	if i >= len(content):
		break

print "xoxo"
uniqueWords = Set([])
for lines in trainBody:
	words = re.split('\s|(?<!\d)[,.]|[,.](?!\d)',lines)
	for word in words:
                word = word.lower()
		if "&" in word or '1' in word or '2' in word or '3' in word or '4' in word or '5' in word or '6' in word or '7' in word or '8' in word or '9' in word or '0' in word or '.' in word or word == 'a' or word == 'the' or word =='an':
			continue
		if "\'s" in word:
			uniqueWords.add(word[:-2])
			continue
		if ")" in word:
			uniqueWords.add(word[:-1])
			continue
		if "(" in word:
			uniqueWords.add(word[2:])
			continue
#		if word[len(word)-1] == 's':
#			if word[:-1] in uniqueWords:
#				continue
#			uniqueWords.add(word)#
		uniqueWords.add(word)
doc_count = {}
set_train_body = list(Set([]))
for body in trainBody:
	to_insert = {}
	s = Set([])
	for x in re.split('\s|(?<!\d)[,.]|[,.](?!\d)',body):
		x=x.lower()
		if "\\" in x or "&" in x or '1' in x or '2' in x or '3' in x or '4' in x or '5' in x or '6' in x or '7' in x or '8' in x or '9' in x or '0' in x or '.' in x or x == 'a' or x == 'the' or x =='an':
			continue
		if "\'s" in x:
			s.add(x[:-2])
			continue
		if ")" in x:
			s.add(x[:-1])
			continue
		if "(" in x:
			s.add(x[2:])
			continue
		if x not in to_insert:
			to_insert[x] = 1
		else:
			to_insert[x]+=1
		s.add(x)
	set_train_body.append(s)
	termFrequency.append(to_insert)

set_test_body = list(Set([]))
for body in testBody:
	to_insert = {}
	s = Set([])
	for x in re.split('\s|(?<!\d)[,.]|[,.](?!\d)',body):
		x=x.lower()
		if "\\" in x or "&" in x or '1' in x or '2' in x or '3' in x or '4' in x or '5' in x or '6' in x or '7' in x or '8' in x or '9' in x or '0' in x or '.' in x or x == 'a' or x == 'the' or x =='an':
			continue
		if "\'s" in x:
			s.add(x[:-2])
			continue
		if ")" in x:
			s.add(x[:-1])
			continue
		if "(" in x:
			s.add(x[2:])
			continue
		if x not in to_insert:
			to_insert[x] = 1
		else:
			to_insert[x]+=1
		s.add(x)
	set_test_body.append(s)

for word in uniqueWords:
	for body in set_train_body:
		if word in body:
			if word in doc_count:
				doc_count[word]+=1
			else:
				doc_count[word] = 1
	i+=1


tf_idf = list(dict())
for dic in termFrequency:
	to_insert = {}
	for k in dic:
		if k not in doc_count:
			print k
			i=i+1
			continue
		to_insert[k] = (1+log(dic[k]))*log(len(trainBody)/float(doc_count[k]))
	tf_idf.append(to_insert)

max = []
for dic in tf_idf:
	maxt = 0
	for k in dic:
		if dic[k] > maxt:
			maxt = dic[k]
	max.append(maxt)

uniqueWordsToIndex = {}
counter = -1
for i in range(len(tf_idf)):
	dic = tf_idf[i]
	for k in dic:
		if (max[i]-dic[k])/float(max[i]) < 0.3 and k not in uniqueWordsToIndex:
			counter=counter+1
			uniqueWordsToIndex[k] = counter

print uniqueWordsToIndex

train_input_vector = []

for lines in set_train_body:

	arr = np.zeros(len(uniqueWordsToIndex))
	for words in lines:
		if words in uniqueWordsToIndex:
			arr[uniqueWordsToIndex[words]] = 1

	train_input_vector.append(arr)

train_input = np.array(train_input_vector)



test_input_vector = []

for lines in set_test_body:

	arr = np.zeros(len(uniqueWordsToIndex))
	for words in lines:
		if words in uniqueWordsToIndex:
			arr[uniqueWordsToIndex[words]] = 1

	test_input_vector.append(arr)

test_input = np.array(test_input_vector)
print "xoxo"
with open("reuters/all-topics-strings.lc.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content] 

topicsToIndex = {}
j = 0
for words in content:
	topicsToIndex[words] = j
	j+=1
topicsToIndex['None'] = j

train_output_vector = []
for lines in trainTopics:
	train_output_vector.append(topicsToIndex[lines[0]])
train_output = np.array(train_output_vector)


test_output_vector = []
for lines in testTopics:
	test_output_vector.append(topicsToIndex[lines[0]])

test_output = np.array(test_output_vector)
print('\nLogistic Regression')

LR = LogisticRegression(tol=0.0001,solver = 'lbfgs', multi_class = 'multinomial', max_iter=1000, verbose =3)
LR.fit(train_input, train_output)
y_pred = LR.predict(test_input)

print('\nLogistic Regression')
print('Accuracy Score: ',metrics.accuracy_score(test_output,y_pred)*100) #76.4%
print('Confusion Matrix: ',metrics.confusion_matrix(test_output,y_pred))


print('\nNeural Networks')
NN = MLPClassifier(hidden_layer_sizes=(1000, 1000), learning_rate_init=0.001, max_iter=200, verbose = 3)
NN.fit(train_input, train_output)
y_pred = NN.predict(test_input)
print('Accuracy Score: ',metrics.accuracy_score(test_output,y_pred)*100) #77.08