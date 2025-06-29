from flask import Flask, request, render_template
from datetime import datetime
import requests
BACKEND_URL = 'http://0.0.0.0:9000'
app = Flask(__name__)

@app.route('/')
def home():
    # day_of_week = datetime.today().strftime('%A')
    # current_time = datetime.now().strftime('%H:%M:%S')

    day_of_week = datetime.today().strftime('%A')
    current_time = datetime.today()
    return render_template('index.html',day_of_week=day_of_week,current_time=current_time)

@app.route("/submit",methods=['POST'])
def submit() :
    form_data = dict(request.form )
    form_data['datetime'] = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    print(form_data)
    res = requests.post(BACKEND_URL+'/submit',json=form_data ).json()
    print("form submitted")
    return res["message"]

@app.route("/submittodoitem",methods=['POST'])
def submittodoitem() :
    form_data = dict(request.form )
    
    print(form_data)
    res = requests.post(BACKEND_URL+'/submittodoitem',json=form_data ).json()
    print("form submitted")
    return res["message"]

@app.route("/api/view")
def view() :
    res = requests.get(BACKEND_URL+"/view").json()
    return res

@app.route("/api/fileview")
def fileview() :
    res = requests.get(BACKEND_URL+"/fileview").json()
    return res

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000,debug=True )