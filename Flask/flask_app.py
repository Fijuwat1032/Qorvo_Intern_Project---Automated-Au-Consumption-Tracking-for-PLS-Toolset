import flask
from flask import request, jsonify

app = flask.Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return "<h1> Flask is working for you!"

@app.route('/get', methods = ['GET', 'POST'])
def get():
    params = request.form.to_dict(flat = True)
    print(params)
    print('hahahhha')
    req = {}
    if(not bool(params)):
        print('Here')
        params = request.get_json(force = True)
        for i in params:
            req[i] = params[i]
    else:
        for i in params:
            req[i] = params[i][0]
    
    org_val = req['Original']
    print(org_val)
    
    if(org_val == 'name'):
        return jsonify({'res' : 'This is Correct'})
    return jsonify({'res' : 'This is NOT Correct'})

if(__name__ == '__main__'):
    app.run()
#app.run(host = '127.0.0.1', port = 80, threaded = True)