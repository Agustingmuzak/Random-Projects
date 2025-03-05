from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/<username>")
def home(username):
    return render_template("index.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)
