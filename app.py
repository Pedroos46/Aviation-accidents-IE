import sys
import threading
import webbrowser
import os

from flask import Flask, render_template, request
from flask_cors import CORS
from modelrun import inference, modelInit

PORT = 80
url = 'localhost'

# command to run: flask run --host=127.0.0.1 --port=5000
app = Flask(__name__)
cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

print("--> Starting up the server.")

modelData = modelInit()

if __name__ == '__main__':
    app.run()

if __name__ == 'app':
    print("--> Server is ready. 🔥")
    #TODO AUTOMATIC OPEN MAIN PAGE

@app.route('/')
def start():  # put application's code here
    return render_template("index.html")


# On localhost:5000/run
@app.route('/run', methods=['GET'])
def run():
    if request.args.get('inputstr') is None:
        return 'Wrong input 🤔🤨'
    else:
        if modelData is None:
            return 'Wrong intialitzation 😵😵‍💫'
        else:
            instr = request.args.get('inputstr')
            try:
                model_response = inference(modelData, instr)
                return model_response
            except:
                print("Oops!", sys.exc_info()[0], "occurred.")
                return "Something went wrong 😔"
