from bs4 import BeautifulSoup
import requests

page = requests.get('https://onepiece.fandom.com/wiki/Chapter_1').text
soup = BeautifulSoup(page, 'lxml')
title = soup.find('aside', class_ = 'portable-infobox pi-background pi-border-color pi-theme-Chapter pi-layout-default')
#finding title of chapter 1 webpage
title_name = soup.find('h2', class_ = 'pi-item pi-item-spacing pi-title pi-secondary-background').text
print(title_name)
#finding chapter number
chapter_num = soup.find('span', 'mw-page-title-main').text

