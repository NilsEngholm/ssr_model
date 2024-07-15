import requests
import time
import datemath

#url = 'https://speedskatingresults.com//index.php?p=17&s='

def pull_age(ID):
    url = f'https://speedskatingresults.com//index.php?p=17&s={ID}'
    content = requests.get(url)
    content = content.content
