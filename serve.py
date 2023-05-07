from flask import Flask, request
import subprocess
import socket
import os
app = Flask(__name__)

path = os.path.dirname(os.path.abspath(__file__))
strees_cpu_file_path = os.path.join(path,"stress_cpu.py")

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/',methods = ['POST'])
def run_stress_cpu():
   p = subprocess.Popen(["python3",strees_cpu_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
   output, errors = p.communicate()
   print(output,errors)
   return output

@app.route('/',methods = ['GET'])
def get_seed():
   myHostName = socket.gethostname()
   myIP = socket.gethostbyname(myHostName)
   return str(myIP)

if __name__ == '__main__':
   #run_stress_cpu()
   app.run(host='0.0.0.0',debug = True)
