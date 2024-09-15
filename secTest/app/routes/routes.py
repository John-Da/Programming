from flask import render_template
from app import app


@app.route('/')
@app.route('/home')
def home():
    return render_template("landingpage.html")


@app.route('/register')
def signup():
    return render_template("register.html")

@app.route('/login')
def login():
    return render_template("login.html")
