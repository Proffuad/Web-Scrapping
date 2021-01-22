from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import requests

html= requests.get('https://www.worldometers.info/coronavirus/country/nigeria/').text
soup= BeautifulSoup(html, 'lxml')
new_cases= soup.find('li', class_= 'news_li').strong.text.split()[0]
deaths= list(soup.find('li', class_= 'news_li').strong.next_siblings)[1].text.split()[0]

# Notifier
notifier= ToastNotifier()
msg= f'New cases: {new_cases}\nDeaths: {deaths}'
notifier.show_toast(title= 'COVID-19 daily update', msg= msg, duration= 10, icon_path= 'virus.ico')