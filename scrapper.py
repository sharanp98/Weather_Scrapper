import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

page = requests.get('https://www.worldweatheronline.com/lang/en-in/trivandrum-weather/kerala/in.aspx')
soup = BeautifulSoup(page.content,'html.parser')

week = soup.find(id='days5_section')

content = week.find(class_='bg_white page_section')
items = content.find_all(class_='carousel-cell well text-center')
date= []
day = []
temp_high = []
temp_low = []
for item in items:
    ls = item.get_text().split()
    day.append(ls[0])
    date.append(ls[1])
    x,y,_ = ls[2].split('°c')
    temp_high.append(x)
    temp_low.append(y)

df = pd.DataFrame( list(zip(day,date,temp_high,temp_low)),columns = ['Day','Date','High','Low']) 
df.to_csv(os.getcwd()+'/weather.csv')