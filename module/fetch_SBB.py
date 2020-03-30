import requests
import json
import math
import time

import Adafruit_CharLCD as LCD


url = "http://transport.opendata.ch/v1/stationboard?station=lucerne&limit=1"

response = requests.get(url)
data = response.text

parsed = json.loads(data)

station = (parsed.get("station").get("name"))
destination = (parsed.get("stationboard")[0].get("to"))
delay = (parsed.get("stationboard")[0].get("stop").get("delay"))
name = (parsed.get("stationboard")[0].get("name"))
number = (parsed.get("stationboard")[0].get("number"))
category = (parsed.get("stationboard")[0].get("category"))
departure = parsed.get("stationboard")[0].get("stop").get("departure")

departure_time = departure[-13:16]