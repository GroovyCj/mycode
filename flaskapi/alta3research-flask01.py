#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
import json
from flask import jsonify

app = Flask(__name__)

goodans = "otacon"

@app.route("/<name>")
def start(name):
    return render_template("landingpage.html",name=name )


@app.route("/answer", methods=["POST"])
def rightornot():
    if request.method == "POST":
        if request.form.get("ans")== "otacon":
            return redirect(url_for("correct"))
        else:
            return redirect(url_for("start",name="captain failure"))




@app.route("/correct")
def correct():
        return "You are correct!"
    

metaldata = [{
    "name" : "Otacon",
    "realname" : "Hal Emmerich",
    "friend" : "Solid Snake",
    "first appearance" : "Metal Gear Solid"},
    { "name" : " Solid Snake",
      "realname" : "David",
      "friend" : "Otacon",
      "first appearance" : "Metal Gear Solid"}]

@app.route("/metal", methods=["GET", "POST"])
def charShow():
    if request.method == "POST":
        data = request.json
        if data:
           data= json.loads(data)
           name = data["name"]
           realname = data["realname"]
           friend = data["friend"]
           firstappearance  = data["first appearance"]
           metaldata.append({"name" : name, "realname":realname, "friend":friend, "first appearance": firstappearance})
    return jsonify(metaldata)










if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

