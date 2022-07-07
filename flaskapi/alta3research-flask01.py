#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
import json


app = Flask(__name__)

goodans = "otacon"

@app.route("/")
def start():
    return render_template("landingpage.html")


@app.route("/answer", methods=["POST"])
def rightornot():
    if request.method == "POST":
        if request.form.get("ans")== "otacon":
            return redirect(url_for("correct"))
        else:
            return redirect(url_for("start"))







@app.route("/correct")
def correct():
        return "You are correct!"
    











if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

