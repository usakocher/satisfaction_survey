from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from mail import send_mail

app = Flask(__name__)

ENV = 'prod'
    
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    colleague = db.Column(db.String(200), unique = True)
    role = db.Column(db.String(200))
    helpful = db.Column(db.Integer)
    commitment = db.Column(db.Integer)
    skills = db.Column(db.Integer)
    overall = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, colleague, role, helpful, commitment, skills, overall, comments):
        self.colleague = colleague
        self.role = role
        self.helpful = helpful
        self.commitment = commitment
        self.skills = skills
        self.overall = overall
        self.comments = comments

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods = ["POST"])
def submit():
    if request.method == 'POST':
        colleague = request.form['colleague']
        role = request.form['role']
        helpful = request.form['helpful']
        commitment = request.form['commitment']
        skills = request.form['skills']
        overall = request.form['overall']
        comments = request.form['comments']
        if colleague == '' or role == '':
            return render_template('index.html', message = 'Please enter the required fields')
        if db.session.query(Feedback).filter(Feedback.colleague == colleague).count() == 0:
            data = Feedback(colleague, role, helpful, commitment, skills, overall, comments)
            db.session.add(data)
            db.session.commit()
            send_mail(colleague, role, helpful, commitment, skills, overall, comments)
            return render_template('success.html', message = '')
        return render_template('index.html', message='You have already submitted')

if __name__ == '__main__':
    app.run()
