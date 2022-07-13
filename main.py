import os
import requests
from twilio.rest import Client

api_key = os.environ.get("OWM_API_KEY")
response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall?"
                            f"lat=YOUR LATITUDE&"
                            "lon=YOUR LONGITUDE&"
                            "exclude=current,minutely,daily"
                            f"&appid={api_key}")
account_sid = os.environ.get("OWM_ACCOUNT_SID")
auth_token = os.environ.get("OWM_AUTH_TOKEN")

response.raise_for_status()
weather_data = response.json()

score = 0
will_rain = False

for _ in range(12):
    hour_data = weather_data["hourly"][score]["weather"][0]["id"]
    score += 1
    if int(hour_data) < 600:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going rain today. Remember to bring an ☂ ",
        from_='YOUR TWILIO NUMBER',
        to='YOUR OWN NUMBER'
    )
    print(message.status)
