import sys
import threading
import webbrowser
import os


from flask import Flask, render_template, request

from modelrun import inference, modelInit

PORT = 80
url = 'localhost'

# command to run: flask run --host=localhost --port=5000

print("\n--> Starting up the server.")
app = Flask(__name__)
modelData = modelInit()


if __name__ == '__main__':
    app.run()
    threading.Timer(1.5, lambda: webbrowser.open_new('www.google.com')).start()
    os.system("open https://google.com")

@app.route('/')
def hello_world():  # put application's code here
    return render_template("else.html")


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
