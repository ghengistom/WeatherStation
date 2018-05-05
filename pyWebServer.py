import importlib

#moduleName = input('Enter module name:')
moduleName = input('getHistoryModel.py')
importlib.import_module(moduleName)


#import os
#os.system("/home/pi/WeatherStation/getHistoryModel.py")

from flask import Flask
app = Flask(__name__)

@app.route('/')
def testing():
   return 'Testing '
