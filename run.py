import os
from flask import Flask, render_template, url_for
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
    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Log-in", form=form)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')),
        debug=True)
