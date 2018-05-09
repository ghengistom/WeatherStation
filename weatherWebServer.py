import getHistoryModel
import gettemp
from flask import jsonify
from flask import Flask, request #import main Flask class and request object

app = Flask(__name__) #create the Flask app


@app.route('/gethistory', methods=['GET']) #GET requests will be blocked
def get_history():
    h = getHistoryModel.getHistory()
    return jsonify(h)


@app.route('/gettemp', method=['GET'])
def get_temp():
    j = gettemp.gettemp_()



@app.route('/test1', methods=['GET']) #GET requests will be blocked
def test1():
    return 'Todo...'   #need to call getHistoryModel.py then return json 



if __name__ == '__main__':
    app.run(host='0.0.0.0')
# if __name__ == '__main__':
#     app.run(debug=True, port=5000) #run app in debug mode on port 5000