#!/usr/bin/python3

# Created By Julian Bruegger
# 29.03.2020
# Questions please contact jul.bruegger(at)gmail.com
# To change country edit ./module/corona.py

from module.i2c import *
import requests
import time
import math
import sys
import json


while True:
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


    if delay == 'None':
        if category == 'RE':
            lcd_init()
            time.sleep(1)
            lcd_string((station)+(" nach ")+(destination),LCD_LINE_1)
            lcd_string((number),LCD_LINE_2)
            lcd_string("Departure:",LCD_LINE_3)
            lcd_string(departure_time,LCD_LINE_4)
            print(station, number, destination, departure_time)
        else:
            lcd_init()
            time.sleep(1)
            lcd_string((station)+(" nach ")+(destination),LCD_LINE_1)
            lcd_string(category+number,LCD_LINE_2)
            lcd_string("Departure:",LCD_LINE_3)
            lcd_string(departure_time,LCD_LINE_4)
            print(station, (category+number), destination, departure_time)
    else : 
        if category == 'RE':
            lcd_init()
            time.sleep(1)
            lcd_string((station)+(" nach ")+(destination),LCD_LINE_1)
            lcd_string(number,LCD_LINE_2)
            lcd_string("Departure:",LCD_LINE_3)
            lcd_string((departure_time)+(" Exp: +")+(delay),LCD_LINE_4)
            print(station, (number), destination, departure_time, delay)
        else:
            print(station, (category+number), destination, departure_time, delay)
            lcd_init()
            time.sleep(1)
            lcd_string((station)+(" nach ")+(destination),LCD_LINE_1)
            lcd_string(category+number,LCD_LINE_2)
            lcd_string("Departure:",LCD_LINE_3)
            lcd_string((departure_time)+(" Exp: +")+(delay),LCD_LINE_4)

    
    
    time.sleep(30)
    