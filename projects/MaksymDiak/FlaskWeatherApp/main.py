import os, requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

WEATHER_API = os.getenv("WEATHER_API_KEY")

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    city = weather_conditions = ""
    temp = wind = humidity = 0

    if request.method == "POST":
        city = request.form["locationInput"]
        if city:
            try:
                link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={WEATHER_API}"
                res = requests.get(link)
                data = res.json()
                weather_conditions = data["weather"][0]["main"].lower()
                temp = int(round(data["main"]["temp"], 0))
                wind = data["wind"]["speed"]
                humidity = data["main"]["humidity"]
            except:
                city = "Error"
                weather_conditions = ""
                temp = wind = humidity = 0

    return render_template(
        "index.html",
        city=city,
        temp=temp,
        wind=wind,
        humidity=humidity,
        weather_conditions=weather_conditions,
    )


if __name__ == "__main__":
    app.run(debug=True)
