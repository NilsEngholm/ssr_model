import requests
import time
from bs4 import BeautifulSoup

#url = 'https://speedskatingresults.com//index.php?p=17&s='

def pull_age(ID):
    url = f'https://speedskatingresults.com//index.php?p=17&s={ID}'
    page = requests.get(url)
    content = page.content
    
    print(content)
    soup = BeautifulSoup(page.text, 'html.parser')
    bday = soup.find('span', class_='date')
    if bday:
        raw_html = str(bday)
        print(raw_html)
    else:
        print('not found')

pull_age(29916)