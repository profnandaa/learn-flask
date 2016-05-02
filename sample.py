from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/login")
def login():
    return "Login Form"

if __name__ == "__main__":
    app.run(port=5001)