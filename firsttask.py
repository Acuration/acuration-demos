import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.moneycontrol.com/india/stockpricequote/diversified/itc/ITC'
page = requests.get(url)
page

soup = BeautifulSoup(page.text,'lxml')
soup

price = soup.find('div', class_ = 'inprice1 nsecp').text
price
