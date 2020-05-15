#   A simple flask based server that interacts with Telegram Bot API
#   May 15/2020

import requests
from flask import Flask
from flask import request
from flask import Response
import json

botToken = "1255494272:AAGxxBEViZAxjrjdNARxH7O-P5SQFA2Dmkg"     # unique telegram bot identifier token
TelegramChannals = []   # list of telegram channals the bot interacts with

app = Flask(__name__)  # Flask server initialization


#   a function that writes a Json file to a file that contains input from a Bot user   
def jsonWrite(data, filename = "file.json"):
    with open(filename,"w") as f:
        json.dump(data,f,indent=4,ensure_ascii=False)

### bot intereaction ####
def basicResponce(msg):
    ide = msg['message']['chat']['id']
    text = msg['message']['text']
    tex = text+" my ass 😁'"
    url = 'https://api.telegram.org/bot{}/sendMessage'.format(botToken)
    payload = {'chat_id':ide,'text':tex}
    r = requests.post(url, json=payload)
    return r
### bot intereaction ####

    
@app.route("/", methods=['POST','GET']) # a flask function decorator, in this caase '/' to a default index page
def index():
    if request.method == "POST":
        msg = request.get_json()
        jsonWrite(msg,"input.json")
        basicResponce(msg)
        return Response('ok', status=200) # this is like the flask telling telegram to 'chill out n stop spaming the flask(this) server, everything is ok :D'
    else:
        return "<h3>Somth Somthn</h3>" # non Bot related GET page, an html tag

if __name__ == "__main__":
	app.run(debug=True, port = 8443)
