from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Userinfo.sqlite3'
app.config['SECRET_KEY'] = "The water is red"

db = SQLAlchemy(app)


class Userinfo(db.Model):
    __tablename__ = "userinfo"
    id = db.Column('user_ph', db.Integer, primary_key=True)
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))

    def __repr__(self):
        return f'<Userinfo {self.fname, self.lname}>'


def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/enter/', methods=('GET', 'POST'))
def enter():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        phno = request.form['phno']

        if not phno or not fname or not lname:
            flash('Please enter all the fields', 'error')
        else:
            user = Userinfo(id=phno, fname=fname, lname=lname)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('enter.html')

@app.route('/cardspage', methods=('GET','POST'))
def cardspage():
    return render_template('cardspage.html')



app.run(host='0.0.0.0', port=81)
