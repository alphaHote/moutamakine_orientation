import similarite as sim
import enrechissement as enr

from flask import Flask, request, render_template

def read_txt(path):
    txt=""
    with open(path, 'r', encoding='utf-8') as fis:
        for line in fis.readlines():
            txt+=line
    return txt

app = Flask(__name__)
x=0
text=""
@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/housni2', methods=['GET'])
def my_form_post():
    global text
    txt=text
    text=""
    ecoles=read_txt("data_depart.txt").split("</ecole>")
    mx=0.0
    choix=""
    for ecole in ecoles:
        s=sim.simhash(ecole,txt)
        # print(s)
        if s>mx:
            mx=s
            choix=ecole
    return "<!DOCTYPE html><html><head></head><body><h1>"+choix+"</h1></body></html>"

@app.route('/housni', methods=['POST'])

def get_text():
    global x
    global text
    #print(type(request.form))
    for it in list(request.form.listvalues()):
        text+=it[0]
    text=enr.enrechir_text(text)
    return "roger that"
