from flask import Flask, redirect, url_for, render_template, request, session
import MusicStore as MS
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "6136b60461acb26616b2e15d0a7b1a8cfb7993f4751d9059a34772a2dc9c2b04"
app.permanent_session_lifetime = timedelta(hours=2)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:    
        if "user" in session:
            return redirect(url_for("user"))
        
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))
 
if __name__ == "__main__":
    app.run(debug=True)


