import requests
from bs4 import  BeautifulSoup as BS

s = requests.Session

auth_html = s.get('https://smartprogress.do/')

auth_bs = BS(auth_html.content, 'html.parser')
csrf = auth_bs.select('input[name=YYI_CSRF_TOKEN]')[0]['value']
print(csrf)