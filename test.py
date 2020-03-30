import requests
import json
import sys
import time

url = "http://transport.opendata.ch/v1/stationboard?station=lucerne&limit=5"

while True:
    response = requests.get(url)
    data = response.text

    parsed = json.loads(data)
    for i in range(5):

        station = (parsed.get("station").get("name"))
        destination = (parsed.get("stationboard")[i].get("to"))
        delay = str(parsed.get("stationboard")[i].get("stop").get("delay"))
        name = (parsed.get("stationboard")[i].get("name"))
        number = (parsed.get("stationboard")[i].get("number"))
        category = (parsed.get("stationboard")[i].get("category"))
        departure = parsed.get("stationboard")[i].get("stop").get("departure")
        departure_time = departure[-13:16]

        if delay == 'None':

            
            if category == 'RE':
                print(station, number, destination, departure_time)
            else:
                print(station, (category+number), destination, departure_time)
        else : 
            
            if category == 'RE':
                print(station, (number), destination, departure_time, delay)
            else:
                print(station, (category+number), destination, departure_time, delay)

            
    for x in range(4):
        print('')
    time.sleep(1)
    
