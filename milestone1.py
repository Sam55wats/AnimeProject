from bs4 import BeautifulSoup
import requests


chapters_page = 'https://onepiece.fandom.com/wiki/Chapter_'
chapter_urls = [f'{chapters_page}{i}' for i in range(1, 201)]
print(chapter_urls)


page = requests.get('https://onepiece.fandom.com/wiki/Chapter_1').text
##print(page)
#soup = BeautifulSoup(page, 'lxml')
#title = soup.find('aside', class_ = 'portable-infobox pi-background pi-border-color pi-theme-Chapter pi-layout-default')

#finding title of chapter 1 webpage
#title_name = soup.find('h2', class_ = 'pi-item pi-item-spacing pi-title pi-secondary-background').text
##print(title_name)

#finding chapter number
#chapter_num = soup.find('span', 'mw-page-title-main').text

#finding short summary
#short_summary = soup.find('span', id = 'Short_Summary').find_next('p').text
#print(short_summary)

#finding long summary
'''long_heading = soup.find('span', id = 'Long_Summary')
contents_after = long_heading.parent.find_next_siblings('p')
long_summary = ""
for paragraph in contents_after:
    long_summary += paragraph.text
#print(long_summary)
'''

