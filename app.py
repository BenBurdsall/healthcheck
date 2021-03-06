from flask import Flask
import os
import socket

VERSION = "APPVERSION"
HN  = "HN"


app = Flask(__name__)

@app.route('/')
def home():

    ver = '(not set)'
    if VERSION in os.environ:
        ver = os.environ[VERSION]

    hostname = "(not set)"
    if HN in os.environ:
        hostname = os.environ[HN]

    return f'<h1> {host} is healthy, running version {ver} </h1> '

if __name__ == '__main__':
    print("webserver starting")
    app.run(debug=True, host='0.0.0.0')