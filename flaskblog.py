from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app=Flask(__name__)

app.config['SECRET_KEY']='bdc35b68e981a0f3a5b11c320705d05c26bbfbaee3c28ff6f809f71575e5c1ab'


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

#home page 
@app.route('/')
@app.route('/home')
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

if __name__=='__main__':
    app.run(debug=True)
