from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['post'])
def login():
    print("logged in")
    uName = request.form['uName']
    pWord = request.form['pWord']
    print(uName, pWord)
    return render_template("loggedIn.html")

if __name__ == '__main__':
    app.run()
