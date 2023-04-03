from flask import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Homepage.html")

if __name__ == ("__main__"):
    app.run()