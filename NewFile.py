#LAST HOMEWORK PY
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<h1>Hello World!</h1>"
@app.route("/home", methods=['POST','GET'])
def home_page():
    return "<h1>It is our home page!</h1>"
@app.route("/store")
def store():
    return "<h1>It is our Store!</h1>"
if __name__ == "__main__":
    app.run(debug=True)


