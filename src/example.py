from datetime import datetime

from flask import Flask

app = Flask(__name__)


@app.route('/getDate')
def getDate():
    return str(datetime.today())
