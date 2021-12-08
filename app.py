import sys
import webbrowser

from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
from modelrun import inference, modelInit

# Sever config | command to run: flask run --host=127.0.0.1 --port=5000
host = '127.0.0.1'
port = 5000
url = 'http://'+host+':'+str(port)

# Flask Settings:
app = Flask(__name__, static_folder='static', template_folder='templates')
# CORS
cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


print("--> Starting up the server.")
modelData = modelInit()

if __name__ == '__main__':
    app.run(host=host, port=port)

if __name__ == 'app':
    print("--> Server is ready. 🔥")
    webbrowser.open(url)


@app.route('/')
def start():
    return render_template("index.html")


@app.route('/run', methods=['GET'])
@cross_origin(origin='127.0.0.1',headers=['Content- Type','Authorization'])
def run():
    if request.args.get('inputstr') is None:
        return 'Wrong input 🤔🤨'
    else:
        if modelData is None:
            return 'Wrong initialization 😵😵‍💫'
        else:
            instr = request.args.get('inputstr')
            try:
                model_response = inference(modelData, instr)
                return model_response
            except:
                print("Oops!", sys.exc_info()[0], "occurred.")
                return "Something went wrong 😔"


##########################################################
# INTERNAL FUNCTIONS OF SERVER:

# Shutdown server without crtl+c
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
