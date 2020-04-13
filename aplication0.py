from flask import Flask
app = Flask(__name__)
saludado="World"
@app.route("/")
def index():
    saludado="World"
    return "Hello, World!"

@app.route("/<string:name>")
def hello(name):
    if name == "h1":
       size="h1"
    if name == "h2":
       size="h2"
    else:
       size="h3"
    return f"<{size}>Hello, {name.capitalize()}!</{size}>"
