#! /usr/bin/pyhton3

from flask import Flask
app = Flask(__name__)

###############################
#url routing
import json
import database as db


@app.route('/')
def hello_world():
    d = {'username': 'cong'}
    result = json.dumps(d)
    return result

@app.route('/userlist')
def get_user_list():
    d = db.get_user()
    result = json.dumps(d)
    return result

@app.route('/test')
def to_test():
    return 'test successful'


###############################

if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run(debug=True)