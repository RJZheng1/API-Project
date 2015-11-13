from flask import Flask,render_template,redirect,request
import getstuff

app = Flask(__name__)
@app.route("/",methods = ["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
         
if __name__ == "__main__":
    app.debug = True
    app.secret_key = "Idk"
    app.run(host = "0.0.0.0", port = 4000)
