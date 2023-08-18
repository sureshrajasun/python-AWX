# import requests module

#python -m pip install flask
# 
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/<templateId>', methods=['POST'])
def createJob(templateId):
   
    response = requests.post('http://3.25.166.250/api/v2/job_templates/'+templateId+'/launch/',auth = HTTPBasicAuth('admin', '********'))
    print(response.status_code)
    repos = response.json()
    print(repos['job'])
    return jsonify({'AWX JOB ID': repos['job']}) 

@app.route('/<jobId>', methods=['GET'])
def fetchJob(jobId):
   
    response = requests.get('http://3.25.166.250/api/v2/jobs/'+jobId, auth = HTTPBasicAuth('admin', '********'))
    #response.headers.add('Access-Control-Allow-Origin', '*')
    print(response.status_code) 
    repos = response.json()
    print("Status-->" + repos['status'])
    print(json.dumps(repos, indent = 4, sort_keys=True))
    return jsonify({'STATUS': repos['status']}) 
    #return response

app.run(debug=True)

