from flask import Flask, request
import subprocess
from datetime import datetime
from os.path import exists
from flask import send_file

app = Flask(__name__)

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'
    
@app.route('/getVoiceList')
def getVoiceList():
    p = subprocess.Popen("c:/balcon/balcon.exe -l", stdout=subprocess.PIPE, shell=True)
    #print(p.wait())
    output, err = p.communicate()
    print(output)
    return output
    
@app.route('/getAudio', methods=['GET'])
def getAudio():
    prompt = request.args.get('prompt')
    print(prompt)
    now = str(datetime.now())
    print(now)
    now = now.replace(" ", "")
    now = now.replace("-", "")
    now = now.replace(":", "")
    print(now)
    #now = "unffddssct3t7865655930r3r" 
    command = "c:/balcon/balcon.exe -n \"VE_American_English_Ava_22kHz\" -t \"Hello there Unmesh, How are you?\" -w \"{}.wav\"".format(now)
    print(command)
    p = subprocess.Popen("c:/balcon/balcon.exe -n \"VE_American_English_Ava_22kHz\" -t \"{}\" -w \"{}.wav\"".format(prompt,now), stdout=subprocess.PIPE, shell=True)

    print(p.wait())
    print(p.communicate())
    p_status = p.wait()
    print(p_status)
    if (p_status == 0):
        print(now)
        file_exists = exists(now+'.wav')
        print(file_exists)
        if(file_exists == True) :
    	    return send_file(now+'.wav')
        else :
    	    return "Some error creating audio"
# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host='0.0.0.0', port=5000)
