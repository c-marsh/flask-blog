import os
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = "a5hMUwAiWMTjgSFq"
posts = [
    {"author": "John Smith",
     "title": "Post 1",
     "content": "Post 1 contents",
     "date": "21/2/2020"},
    {"author": "Jane Doe",
     "title": "Post 2",
     "content": "Post 2 contents",
     "date": "22/2/2020"}

]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
            if form.email.data == "cmhilfiker@gmail.com" and form.password.data == "password":
                flash("You've been successfully logged in!", "success")
                return redirect (url_for("home"))
            else:
                flash ("Login failed, please check your email and password.", "danger")
    return render_template("login.html", title="Log-in", form=form)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')),
        debug=True)
