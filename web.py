#!/usr/bin/python

from flask import Flask
from flask import render_template
import os

app = Flask(__name__)

env=os.getenv('ENV')

@app.route('/liveness')
def healthx():
  time.sleep(2);
  return "<h1><center>Liveness check completed</center><h1>"
  
@app.route('/readiness')
def healthz():
  time.sleep(20);
  return "<h1><center>Readiness check completed</center><h1>"

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/picture")
def pic():
        return render_template('index.html')

@app.route("/pragmatic")
def salvador():
    result= f"hello from {env}"
    return result
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=30000)
