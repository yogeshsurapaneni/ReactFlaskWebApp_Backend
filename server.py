from flask import Flask
from waitress import serve
import platform
import psutil



app = Flask(__name__)

#Members API route

@app.route("/host")
def host():

    hostname=platform.node()
    ram=psutil.virtual_memory().percent
    final_ret = {"hostname": hostname, "ram": ram}

    return final_ret
if __name__ == "__main__": 
    serve(app, host='0.0.0.0', port=5000)
