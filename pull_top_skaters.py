from bs4 import BeautifulSoup
import pandas as pd
import requests
import os
import time

# topn api call example 'https://speedskatingresults.com/api/xml/topn?gender=f&season=2023&distance=500&country=6&max=3'

# relevant distances
mens_distances = [500, 1000, 1500, 5000, 10000]
womens_distances = [500, 1000, 1500, 3000, 5000]
year = list(range(2014, 2024))
gender = ['f', 'm']


def make_masterlist(sex, year, distance, quantity):
    # make request
    url = f'https://speedskatingresults.com/api/xml/topn?gender={sex}&season={year}&distance={distance}&max={quantity}'
    response = requests.get(url)
    if response.status_code == 200:
        try:
            return ET.fromstring(response.content)
        except ET.parseerror:
            print(f'error getting data for {distance}m from {year}')
            return None
    