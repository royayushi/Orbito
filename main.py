from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

#db = SQLAlchemy(app)
#class userinfo(db.Model):
   #id = db.Column('user_ph', db.Integer(20), primary_key = True)
   #fname = db.Column(db.String(100))
   #lname = db.Column(db.String(100))

#def __init__(self, fname, lname):
   #self.fname = fname
   #self.lname = lname

@app.route('/')
def index():
    return render_template('index.html')


app.run(host='0.0.0.0', port=81)
