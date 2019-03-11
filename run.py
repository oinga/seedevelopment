from flask import Flask, request, render_template, redirect, url_for
from os import environ
from flask_mail import Mail, Message

"""
Routes and views for the flask application.
"""

from datetime import datetime

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'email@email.com'
app.config['MAIL_DEFAULT_SENDER'] = 'email@email.com'
app.config['MAIL_PASSWORD'] = '****'

@app.route('/')
@app.route('/home')
def home():
    """Render the Index/Home page."""
    return render_template(
        'index.html'
    )

@app.route('/about')
def about():
    """Render My Team Page"""
    return render_template(
        'about.html'
        )

@app.route('/blog')
def blog():
    """Render My About Page"""
    return render_template(
        'blog.html'
        )




@app.route('/contact')
def contact():
    """Render My contact Page"""
    return render_template(
        'contact.html'
        )

@app.route('/contact', methods=['GET', 'POST'])
def sendMail():
    if request.method == 'POST':
        msg = Message(request.form['name'],request.form['email'],request.form['message'])
        mail.send(msg)
        return redirect(url_for('home'))


@app.route('/services')
def services():
    """Render My Work Page"""
    return render_template(
        'work.html'
        )

@app.route('/work')
def work():
    """Render My About Page"""
    return render_template(
        'work.html'
        )

@app.route('/work-single')
def workSingle():
    """Render My About Page"""
    return render_template(
        'work-single.html'
        )

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
