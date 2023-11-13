import requests
import os
import sys
import json
import geonamescache
from dotenv import load_dotenv
import random
from time import sleep
import logging


load_dotenv()
API_KEY = os.getenv("API_KEY")
POD_NAME = os.environ.get('MY_POD_NAME')
NODE_NAME = os.environ.get('MY_NODE_NAME')

def custom_logger():
    logger = logging.getLogger("log")
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    logger.addHandler(ch)
    return logger


logger = custom_logger()


def main():
    gc = geonamescache.GeonamesCache()
    countries = gc.get_countries_by_names()
    # print countries dictionary
    list_countries = list(countries.keys())
    top5_countries = random.choices(list_countries, k=5)

    locations = []
    for i in range(0, len(top5_countries)):
        locations.append({"q": top5_countries[i], "custom_id": i + 1})

    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q=bulk"
    payload = json.dumps({"locations": (locations)})
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)
    response = response.json()
    for i in range(0, len(top5_countries)):
        query = response['bulk'][i]['query']
        city = query['q']
        date = query['current']['last_updated']
        temp = query['current']['temp_c']
        logger.info(f'Node: {NODE_NAME}, Pod: {POD_NAME} - At {date}, the temperature in {city} is: {temp}°C')


if __name__ == '__main__':
    while True:
        main()
        sleep(300)