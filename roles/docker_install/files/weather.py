#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module does get weather from openweathermap.org"""
from os import getenv
import pyowm
import pprint


def get_weather():
    """
    Get weather from https://openweathermap.org/api
    :return: dict with some parameters
    """
    owm = pyowm.OWM(getenv('OPENWEATHER_API_KEY'))
    observation = owm.weather_at_place(getenv('CITY_NAME'))
    w = observation.get_weather()

    return {'source': 'openweathermap', 'city': getenv('CITY_NAME'),
            'current_time': observation.get_reception_time(timeformat='iso') + ' UTC+0',
            'description': w.get_detailed_status(), 'humidity': w.get_humidity(),
            'humidity': w.get_humidity(), 'temp': w.get_temperature('celsius')['temp']
            }


if __name__ == "__main__":
    pprint.pprint(get_weather())
