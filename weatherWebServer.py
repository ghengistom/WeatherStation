#!/usr/bin/env python

import getHistoryModel
import gettemp
from flask import jsonify
from flask import Flask, request, render_template #import main Flask class and request object
from flask_cors import CORS
import getTempAve


app = Flask(__name__) #create the Flask app
CORS(app)

@app.route('/gethistory', methods=['GET']) #GET requests will be blocked
def get_history():
 
    h = getHistoryModel.getHistory()
    return jsonify(h)


@app.route('/gettemp', methods=['GET'])
def get_temp():
    j = gettemp.gettemp_()
    return jsonify(j)

@app.route('/SinglePage', methods=['GET'])
def singlePage():
    return render_template('singlePage.html')
    #response = render_template('singlePage.html')
    #response.headers.add('Access-Control-Allow-Origin', '*')
    #return response
    

@app.route('/gethistorypage', methods=['GET'])
def get_historypage():
    return render_template('gethistory.html')

@app.route('/gettempave', methods=['GET'])
def get_tempAve():
    tempave = getTempAve.getTempAve()
    return jsonify(tempave)


@app.route('/test1', methods=['GET']) #GET requests will be blocked
def test1():
    return 'Todo...'   #need to call getHistoryModel.py then return json 



if __name__ == '__main__':
    context = ('ca-certificates.crt', 'privateKey.key')
    app.run( threaded = True, host='0.0.0.0', port = 9000, debug = False )
# if __name__ == '__main__':
#     app.run(debug=True, port=5000) #run app in debug mode on port 5000
