# Creates a dynamic webpage at port 5001 that accepts user-submitted haiku poetry
# Checks the submission for syllable count, strips special characters
# Creates a folder path using the haiku if the syllable test is successful

# Hacked together by Taylor Hokanson
# Based on the work of Armin Ronacher (http://flask.pocoo.org/)


import os
import re
from pathlib import Path
from textstat.textstat import textstat
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)


@app.route('/_get_poem')
def get_poem():
	a = request.args.get('a')
	
	# remove any special characters except for spaces
	a = re.sub('[^A-Za-z ]+', '', a)

	# check syllable count
	numSyl = textstat.syllable_count(a)

	# create a list of individual words
	txtSplit = a.split()

	# convert to path and create directories
	newPath = os.path.join(*txtSplit)
	path = Path(newPath)

	# allow for some slop because the syllable algorithm is imperfect
	if numSyl > 16 and numSyl < 18:
		# add the first part of the absolute path
		pathPrefix = "/home/pi/Desktop/haiku/poems/"
		# combine it with the poem
		fullPath = pathPrefix + str(path)
		# make the missing directories, ignore existing directories
		os.makedirs(fullPath,exist_ok=True)
		
		return jsonify(result = "Score " + str(numSyl) + " " + u"\U0001F61D")
	else:
		return jsonify(result = "Score " + str(numSyl) + " " + u"\u2639")

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	# the host thing needs to be here
	app.run(debug=True, host='0.0.0.0', port=5001)

