from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "The water is red"

db = SQLAlchemy(app)
class userinfo(db.Model):
   id = db.Column('user_ph', db.Integer, primary_key = True)
   fname = db.Column(db.String(100))
   lname = db.Column(db.String(100))

def __init__(self, fname, lname):
   self.fname = fname
   self.lname = lname

@app.route('/')
def enter():
    return render_template('enter.html')

@app.route('/enter', methods=('GET', 'POST'))
def create():
  if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        phno = request.form['phno']

        if not phno or not fname or not lname:
            flash('Please enter all the fields', 'error')
        else:
            user = userinfo(fname, lname, phno)
         
            db.session.add(user)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('enter'))
  return render_template('enter.html')

with app.app_context():
  if __name__ == '__main__':
    db.create_all()
  
app.run(host='0.0.0.0', port=81)
