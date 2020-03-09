import requests
import json


url = "http://transport.opendata.ch/v1/stationboard?station=lucerne&limit=1"

response = requests.get(url)
data = response.text

parsed = json.loads(data)

station = repr(parsed.get("station").get("name"))
destination = repr(parsed.get("stationboard")[0].get("to"))
delay = repr(parsed.get("stationboard")[0].get("stop").get("delay"))
name = repr(parsed.get("stationboard")[0].get("name"))
departure = parsed.get("stationboard")[0].get("stop").get("departure")

print(station, name, destination, delay, departure)
