import requests
from twilio.rest import Client

api_key = "API_KEY"
MY_LAT = 19.567320
MY_LONG = 81.368100

account_sid = 'ACe567fe776d0b2beb6e849c79c94e8690'
auth_token = 'AUTH_TOKEN'

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,daily,minutely",
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][0:12]

will_rain = False

for hour_data in weather_slice:
    if hour_data["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_='+twilio number',
        to='+your number'
    )
    print(message.status)