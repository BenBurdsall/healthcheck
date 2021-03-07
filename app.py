from flask import Flask,Response
import os
from filelistener import FileListener

VERSION = "APPVERSION"
HN  = "HN"

fl = FileListener('/app/logfile.log',60)
fl.monitor()

app = Flask(__name__)


@app.route('/')
def home():


    if not fl.isFileBeingModified():
        print("File is not healthy - causing an HTTP error code ")
        status_code = Response(status=500)
        return status_code

    ver = '(not set)'
    if VERSION in os.environ:
        ver = os.environ[VERSION]

    hostname = "(not set)"
    if HN in os.environ:
        hostname = os.environ[HN]

    return f'<h1> {hostname} is healthy, running version {ver} </h1> '

if __name__ == '__main__':
    print("webserver starting")
    app.run(debug=True, host='0.0.0.0')