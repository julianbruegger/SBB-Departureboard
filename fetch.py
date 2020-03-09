import requests
import json
import math
import time

import Adafruit_CharLCD as LCD


url = "http://transport.opendata.ch/v1/stationboard?station=lucerne&limit=1"

# Raspberry Pi configuration:
lcd_rs = 27  # Change this to pin 21 on older revision Raspberry Pi's
lcd_en = 22
lcd_d4 = 25
lcd_d5 = 24
lcd_d6 = 23
lcd_d7 = 18
lcd_red   = 4
lcd_green = 17
lcd_blue  = 7  # Pin 7 is CE1
# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_RGBCharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                              lcd_columns, lcd_rows, lcd_red, lcd_green, lcd_blue)
while True:
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
    departure_delay = departure[-4:22]

    if departure_delay < "02":

        print(station, destination, delay, departure_time, departure_delay)

        lcd.set_color(0.9, 0.1, 0.1)
        lcd.clear()
        lcd.message(category + number +' to ' + destination)
        lcd.message('\nExp: ' + departure_time + departure_delay)

        time.sleep(60)
    else:
        print(station, destination, delay, departure_time, departure_delay)

        lcd.set_color(0.1, 0.1, 0.1)
        lcd.clear()
        lcd.message(category + number +' to ' + destination)
        lcd.message('\nExp: ' + departure_time )

        time.sleep(30)