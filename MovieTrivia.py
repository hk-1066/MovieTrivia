from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import models
#from models import User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///DATA.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/addUser', methods=['post'])
def addUser():
    print("in login")

    uName = request.form['uName']
    pWord = request.form['pWord']

    # print(uName, pWord)

    nUser = models.User()
    nUser.username = uName
    nUser.password = pWord
    db.session.add(nUser)
    db.session.commit()

    # print("commit data")

    return render_template("loggedIn.html")

@app.route('/getUser', methods=['get'])
def getUser():
    print("get user")

    nUser = models.User()
    users = models.User.query.all()

    for u in users:
        print(u.id, u.username, u.password)

    return render_template("loggedIn.html")


if __name__ == '__main__':
    app.run()
