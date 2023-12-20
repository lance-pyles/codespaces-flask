from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/API", methods=["GET"])
def hello_world2():
    data = { 
            "Modules" : 15, 
            "Subject" : "Data Structures and Algorithms", 
        } 
  
    return jsonify(data)