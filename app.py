from flask import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Homepage.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("error_404.html"), 404

if __name__ == ("__main__"):
    app.run()