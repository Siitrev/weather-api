import pandas as pd
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>", methods=["GET"])
def about(station: str, date: str):
    staid = station.rjust(6, "0")
    filepath = f"data/TG_STAID{staid}.txt"
    df = pd.read_csv(filepath, skiprows=20, parse_dates=["    DATE"])

    temperature = df[df["    DATE"] == date]["   TG"].squeeze()/10
    return {"date:": date, "station": staid, "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True)
