from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import RegistrationForm, LoginForm


# Flask constructor takes the name of current module (__name__)
app=Flask(__name__)
app.config['SECRET_KEY']='bdc35b68e981a0f3a5b11c320705d05c26bbfbaee3c28ff6f809f71575e5c1ab'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)

with app.app_context():
    db.create_all()

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(20), unique=True, nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    image_file=db.Column(db.String(20), nullable=False, default='default.jpg')
    password=db.Column(db.String(60), nullable=False)
    posts=db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}','{self.image_file}')"

class Post(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100), nullable=False)
    date_posted=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content=db.Column(db.Text, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}', '{self.user_id}')"

posts=[
    {
        'author':'Corey Scafer',
        'title':'Blog Post 1',
        'Content':'First post content',
        'date_posted':'April 20,2018',
    },
    {
        'author':'Elie',
        'title':'Blog Post 2',
        'Content':'second post content',
        'date_posted':'April 24,2018',
    }
]

# Python decorator that Flask provides to assign URLs in our app
@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html', posts=posts)

#the about page 
@app.route('/about')
def about():
    return render_template('about.html', title="About")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data=='admin@blog.com' and form.password.data=='password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
             flash(f'Login Unsuccessful. incorrect email or password', 'danger')
    return render_template('login.html', title="Login", form = form)



# Used to execute some code only if the file was run directly, and not imported
if __name__=='__main__':
    app.run(debug=True)
