from flask import Flask 
app=Flask(__name__)

#home page 
@app.route('/')
@app.route('/home')
def home():
    return '<h3> Hello World!</h3>'

#the about page 
@app.route('/about')
def about():
    return '<h3> This is about page</h3>'





if __name__=='__main__':
    app.run(debug=True)