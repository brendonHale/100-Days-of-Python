import requests
from datetime import datetime

# Calgary
MY_LAT = 51.048615
MY_LON = -114.070847

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "formattetd": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()

# Get the hour
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now().hour