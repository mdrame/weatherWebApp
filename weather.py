from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__) # initiating flask class for project


@app.route('/') # creating bridge
def home():
    return render_template("index.html")

# curl https://api.openweathermap.org/data/2.5/weather?q=London&appid=8b8286cb872c5238a1941724160e04b9


@app.route('/weather')
def weather():
    APP_ID = '6b7fda170a093cef98d8ee2fb042472b'
    WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"
    user_input = request.args.get("q")

    # params = {"q" : user_input,  "appid" : APP_ID}
    params = {
    'q': user_input,
    'appid': APP_ID
    }

    cities = {"Paris": "Paris 🗼", "New York": "New York 🗽", "London": "London 🏫"}

    #threeCities {}

    #user input API call
    r = requests.get(WEATHER_URL,params=params)

    # code needs error handling
    weather_result = r.json()

    temp = weather_result["main"]["temp"]




    return render_template("weather.html", user_input=user_input,weather_result=weather_result, temp=temp)



if __name__ == "__main__":
    app.run(debug=True)
