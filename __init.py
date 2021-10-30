from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

    if_name__=="__maindebug=None,
      app.run(debug=True)