from sets import Set
from math import log
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

uniqueWords = Set([])
for lines in trainBody:
	words = lines.split(" ")
	for word in words:
		if " " in word or "&" in word or '1' in word or '2' in word or '3' in word or '4' in word or '5' in word or '6' in word or '7' in word or '8' in word or '9' in word or '0' in word or '.' in word:
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
		uniqueWords.add(word)
doc_count = {}
set_train_body = list(Set([]))
for body in trainBody:
	to_insert = {}
	s = Set([])
	for x in body.split(" "):
		if x not in to_insert:
			to_insert[x] = 1
		else:
			to_insert[x]+=1
		s.add(x)
	set_train_body.append(s)
	termFrequency.append(to_insert)


i = 1

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
			continue
		to_insert[k] = (1+log(dic[k]))*log(len(trainBody)/float(doc_count[k]))
	tf_idf.append(to_insert)

print tf_idf


