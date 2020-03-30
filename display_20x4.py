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



while True:
    from module.fetch_SBB import *
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
            lcd_string((departure_time)+(" Exp: +")+delay,LCD_LINE_4)
            print(station, (number), destination, departure_time, delay)
        else:
            print(station, (category+number), destination, departure_time, delay)
            lcd_init()
            time.sleep(1)
            lcd_string((station)+(" nach ")+(destination),LCD_LINE_1)
            lcd_string(category+number,LCD_LINE_2)
            lcd_string("Departure:",LCD_LINE_3)
            lcd_string((departure_time)+(" Exp: +")+delay,LCD_LINE_4)

    
    
    time.sleep(30)
    