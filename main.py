import pandas
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>", methods=["GET"])
def about(station, date):
    return {"temp:": 25}


if __name__ == "__main__":
    app.run(debug=True)
