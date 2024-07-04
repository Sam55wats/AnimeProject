from bs4 import BeautifulSoup
import requests

class AnimeScraper:
    BASE_URL = 'https://onepiece.fandom.com/wiki/Chapter_'
    CHAPTER_COUNT = 200

    def __init__(self, base_url, chapter_count):
        self.base_url = base_url
        self.chapter_count = chapter_count
        self.chapter_urls = self.get_chapter_urls()
    
    def get_chapter_urls(self):
        return [f'{self.base_url}{i}' for i in range(1, self.count + 1)]

    def get_page_content(self, url):
        page = requests.get(url).text
        return BeautifulSoup(page, 'lxml')

    def get_chapter_title(self, soup):
        return soup.find('h2', class_ = 'pi-item pi-item-spacing pi-title pi-secondary-background').text

    def get_chapter_num(self, soup):
        return soup.find('span', 'mw-page-title-main').text

    def get_short_summary(self, soup):
        return soup.find('span', id = 'Short_Summary').find_next('p').text

    def get_long_summary(self, soup):
        long_heading = soup.find('span', id = 'Long_Summary')
        contents_after = long_heading.parent.find_next_siblings('p')
        long_summary = ""
        for paragraph in contents_after:
            long_summary += paragraph.text
        return long_summary
