from flask import render_template
from app import app
from app.form import Loginform

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Patrick'}    
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login')
def login():
    form = Loginform()
    return render_template('login.html', title='Sign In', form=form)
