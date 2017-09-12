# Creates a dynamic webpage at port 5000 indexes a static diretory listing

# Hacked together by Taylor Hokanson
# Based on the work of Heungsub Lee (https://pythonhosted.org/Flask-AutoIndex/)


import os.path
from flask import Flask
from flask.ext.autoindex import AutoIndex

app = Flask(__name__)
# AutoIndex(app, browse_root=os.path.curdir)
AutoIndex(app, '/home/pi/Desktop/haiku/poems', add_url_rules=True)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)
