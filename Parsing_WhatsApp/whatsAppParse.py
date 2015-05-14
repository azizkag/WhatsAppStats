#this file reads the what'sApp .txt output to generate a nice web interface
import codecs
import re

def parseTxtFile(filepath, outputname):
	#takes the file path to a what'sApp.txt chat and generates a python output
	#every line of the input file is as follows

	#date, time: number: message

	#note: message can be multiline 


	f = codecs.open(filepath,  "r", "UTF-8")
	data = f.read() #reads the entire file as a string
	f.close()

	reg = "((\d+/\d+/\d+), (\d+:\d+:\d+ [AP]M):(.+):([\s\S]*?(?=\d+/\d+/\d+)))"
	#SPLIT EACH MESSAGE TO A SEPARATE LINE
	#group1: everything
	#group2: date
	#group3: time
	#group4: sender
	#group5: message
	regex = re.compile(reg)
	m = regex.findall(data)
	# print data

	html = startHTML()
	for entity in m:
		date = entity[1]
		time = entity[2]
		sender = entity[3]
		message = entity[4]

		html += generateHTMLblock(date, time, sender, message)

	html += endHTML()

	writeHTML(html, outputname)
	print m[5]

def writeHTML(string, name):
	text_file=codecs.open(name, "w", "UTF-8")
	text_file.write(string)
	text_file.close()

def generateHTMLblock(date, time, sender, message):

	newMes = message.replace('\n', '<br>')
	block = """
	<div class="block">
			<div class="sender">%s</div>
			<div class="time">%s %s</div>
			<div class="message"><p>%s</p></div>
	</div>
	""" % (sender, date, time, newMes)

	return block


def startHTML():
	var = """
	<!DOCTYPE html>
	<html lang="en"> 
		<head>
			<link rel="stylesheet" type="text/css" href="styling.css">
			<meta charset="utf-8"/>
			<title>this is the title</title>
		</head>

		<body>

	"""

	return var

def endHTML():
	var = """

	 	</body>
	</html>
	"""
	return var

parseTxtFile('resources/chat1.txt', 'chat1.html ')


