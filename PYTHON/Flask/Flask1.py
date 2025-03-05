from flask import Flask, render_template, url_for
import os

STATIC_DIR = os.path.abspath('./static')
app = Flask(__name__, static_folder=STATIC_DIR)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
        app.run(debug=True)