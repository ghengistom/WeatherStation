import os
os.system("getHistoryModel.py")

from flask import Flask
app = Flask(__name__)

@app.route('/')
def testing():
   return 'Testing '
