import pandas as pd
import requests 
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=34.05361000000005&lon=-118.24549999999999")

soup = BeautifulSoup(page.content, 'html.parser')


week = soup.find(id='seven-day-forecast-body')

#print(week)

items = week.find_all(class_='tombstone-container')
#print('Item 0 >>>>>>', items[0])

print('Period-name: ',items[0].find(class_='period-name').get_text())
#print('Short-desc: ', items[0].find(class_='short-desc').get_text())
#print('temp: ',items[0].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
tempertures = [item.find(class_='temp').get_text() for item in items]

#print(period_names)
#print(short_descriptions)
#print(tempertures)

weather_stuff = pd.DataFrame(
    {
     'period': period_names,
     'short_descrptions': short_descriptions,
     'temprature': tempertures,
    }
)
print(weather_stuff)

weather_stuff.to_csv('weather.csv')

