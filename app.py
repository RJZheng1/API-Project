from flask import Flask,render_template
from flask import redirect,url_for
import getstuff

app = Flask(__name__)
@app.route("/",methods = ["GET","POST"])
def home():
    return render_template("home.html")
