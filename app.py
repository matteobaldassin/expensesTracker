from flask import Flask
#from flask_mysqldb import MySQL

app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello world2!"


if __name__ == "__main__":
    app.run()
