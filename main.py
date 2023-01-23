import pandas as pd
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

table_df = pd.read_csv("data/stations.txt", skiprows=17)
table_df = table_df[["STAID", "STANAME                                 "]]


@app.route("/")
def home():
    return render_template("home.html", table=table_df.to_html())


@app.route("/api/v1/<station>/<date>")
def certain_date(station: str, date: str):
    staid = station.rjust(6, "0")
    filepath = f"data/TG_STAID{staid}.txt"
    df = pd.read_csv(filepath, skiprows=20, parse_dates=["    DATE"])

    temperature = df[df["    DATE"] == date]["   TG"].squeeze() / 10
    return {"date:": date, "station": staid, "temperature": temperature}

@app.route("/api/v1/<station>")
def station_data(station: str):
    staid = station.rjust(6, "0")
    filepath = f"data/TG_STAID{staid}.txt"
    df = pd.read_csv(filepath, skiprows=20, parse_dates=["    DATE"])

    return df.to_dict(orient="records")

@app.route("/api/v1/year/<station>/<year>")
def certain_year(station: str, year: str):
    staid = station.rjust(6, "0")
    filepath = f"data/TG_STAID{staid}.txt"
    df = pd.read_csv(filepath, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result


if __name__ == "__main__":
    app.run(debug=True)
