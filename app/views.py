from app import app

from flask import render_template

"""""
This file contains the most common paths any blog should have. I have implemeted a mvc
desing partern in order to take itsadvantages
"""""
@app.route("/home")
def index ():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/socialnetworks")
def portfolio ():
    return render_template("social.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")