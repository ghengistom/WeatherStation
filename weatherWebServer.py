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


@app.route('/gettempave', methods=['GET'])
def get_tempAve():
    tempave = getTempAve.getTempAve()
    return tempave



if __name__ == '__main__':
    context = ('ca-certificates.crt', 'privateKey.key')
    app.run( threaded = True, host='0.0.0.0', port = 80, debug = False )
# if __name__ == '__main__':
#     app.run(debug=True, port=5000) #run app in debug mode on port 5000
