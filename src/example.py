from datetime import datetime

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/getDate')
def getDate():
    return '"' + str(datetime.today()) + '"'
