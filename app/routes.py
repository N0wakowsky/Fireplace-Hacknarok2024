from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("join.html")

@app.route("/main")
def main():
    return f"GOwno1"

@app.route("/fireplacemaster")
def host():
    test_list = ['Apple', 'Banana', 'Orange', 'Grapes']
    return render_template("fireplacemaster.html", test_list=test_list)
