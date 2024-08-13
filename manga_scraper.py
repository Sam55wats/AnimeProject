from scraper import Scraper

class MangaScraper(Scraper):
    BASE_URL = 'https://onepiece.fandom.com/wiki/Chapter_'
    CHAPTER_COUNT = 200
    DIRECTORY = 'MangaChapters'

    def __init__(self, base_url, episode_count):
        super().__init__(base_url, episode_count)

    def get_characters(self, soup):
        char_section = soup.find('table', {'class': 'CharTable'})
        characters = []

        if char_section:
            char_list = char_section.find_all('li')
            characters = [li.text.strip() for li in char_list]
        
        return characters
   
def main():
    scraper = MangaScraper(MangaScraper.BASE_URL, 200)
    scraper.scrape(MangaScraper.DIRECTORY)

if __name__ == "__main__":
    main()
