import os
from flask import Flask, render_template, url_for
app = Flask(__name__)
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


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')),
        debug=True)
