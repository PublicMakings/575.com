"""
This Flask app connects Javascript and Python
Users enter a haiku online, which this script checks for errors and converts to a filepath on the server

Hacked together by Taylor Hokanson for the Opposable Thumbs Podcast
Based, in part, on the work of Armin Ronacher
"""

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
                pathPrefix = "/home/pi/Desktop/haiku/templates/"

				# combine it with the poem
                fullPath = pathPrefix + str(path)

                # make the missing directories, ignore existing directories
                os.makedirs(fullPath,exist_ok=True)

                return jsonify(result=fullPath)
        else:
                return jsonify(result="Incorrect number of syllables!")

@app.route('/')
def index():
        return render_template('index.html')

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')                
