from flask import Flask, render_template, url_for
app=Flask(__name__)


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
if __name__=='__main__':
    app.run(debug=True)