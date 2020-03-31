import requests
import json
import math
import time

url = "http://transport.opendata.ch/v1/stationboard?station=lucerne&limit=1"

response = requests.get(url)
data = response.text

parsed = json.loads(data)

station = str(parsed.get("station").get("name"))
destination = str(parsed.get("stationboard")[0].get("to"))
delay = str(parsed.get("stationboard")[0].get("stop").get("delay"))
name = str(parsed.get("stationboard")[0].get("name"))
number = str(parsed.get("stationboard")[0].get("number"))
category = str(parsed.get("stationboard")[0].get("category"))
departure =str(parsed.get("stationboard")[0].get("stop").get("departure"))

departure_time = departure[-13:16]