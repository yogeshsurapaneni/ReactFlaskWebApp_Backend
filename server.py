from flask import Flask
import platform
import psutil

app = Flask(__name__)

#Members API route

@app.route("/host")
def host():

    hostname=platform.node()
    ram=psutil.virtual_memory().percent
    return {"host":[hostname,ram]}

if __name__ == "__main__":
    app.run(debug=True)
