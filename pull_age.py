import requests
import time
from bs4 import BeautifulSoup
import pandas as pd

#url = 'https://speedskatingresults.com//index.php?p=17&s='

def pull_age(ID):
    url = f'https://speedskatingresults.com//index.php?p=17&s={ID}'
    page = requests.get(url)
    content = page.content
    
    soup = BeautifulSoup(page.text, 'html.parser')
    bday = soup.find('span', class_='date')
    if bday:
        raw_html = str(bday)
        raw_html = raw_html.replace('<span class="date">', '')
        raw_html = raw_html.replace('</span>', '')
    else:
        print('not found')
    
    return(raw_html)

# read master list df
df = pd.read_csv('C:\\Users\\Nilse\\ssr_model\\Formatted masterlist.csv', usecols=[0])
IDs = set(df['ID'].tolist())

age = []

for i in IDs:
    x = i,pull_age(i)
    if i not in age:
        age.append(x)
        time.sleep(.1)
        print(f'Skater {i} bday is {x}')
    else:
        print('Skater bday already in list')
    #print(age)

age_list = pd.DataFrame(age)
age_list.to_csv('id and bday.csv', index=False)