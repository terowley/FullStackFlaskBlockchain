# test platform for Flask/w3
#
import json

from flask import Flask, Response, request, jsonify, render_template

app = Flask(__name__)



@app.route("/", methods=['GET', 'POST']) 
def home():
    title = "Learning Flask Jango/Forms"
    return render_template("index.html", title = title)

@app.route("/form", methods=['GET', 'POST']) 
def form():
    if request.method == "POST":
        name = request.form.get('Name')
        address = request.form.get('Address')
        return render_template("status.html",name=name,address=address)
     
    return render_template("index.html") 
