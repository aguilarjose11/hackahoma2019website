from flask import Flask, render_template, request, redirect, url_for, flash, session, abort
from flask_cors import CORS
from models import get_posts, create_post, authenticate

app = Flask(__name__)
'''
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_post(name, post)

    posts = get_posts()

    return render_template('index.html', posts=posts)
'''

'''
    This is going to be the view for the first page. (aka. home)
    we will have three buttons, one for each type of registration and one for loging in.
'''
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form['LoginType'] == 'Sponsor Registration':
            return redirect(url_for('sponsor_registration'))
        if request.form['LoginType'] == 'Entrepreneur Registration':
            return redirect(url_for('entrepreneur_login'))
        if request.form['LoginType'] == 'login':
            return redirect(url_for('login'))

    return render_template('home.html')

'''
    This is the login method.
    Here we will deal with al of the login process.
'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        # if request.form['username'] != 'admin' or request.form['password'] != 'admin':
        if authenticate(request.form['username'], request.form['password']):
            return redirect(url_for('swipe'))
        else:
            error = 'Invalid Credentials. Please try again.'

    return render_template('login.html', error=error)

'''
    This is the sponsor registration website.
    TODO: NOT IMPLEMENTED YET
'''
@app.route('/sponsor_registration', methods=['GET', 'POST'])
def sponsor_registration():
        if request.method == 'POST':
            if request.form['reg'] == "Confirm":
                return redirect(url_for('login'))
        return render_template('create.html')

'''
    This is the entrepreuner registration website
    TODO: NOT IMPLEMENTED YET
'''
@app.route('/entrepreneur_login', methods=['GET', 'POST'])
def entrepreneur_login():
    if request.method == 'POST':
        if request.form['reg'] == "Confirm":
            return redirect(url_for('login'))


    return render_template('create.html')

@app.route('/swiper', methods=['GET', 'POST'])
def swipe():
    return render_template('swiper.html')


if __name__ == '__main__':
    app.run(debug=True)
