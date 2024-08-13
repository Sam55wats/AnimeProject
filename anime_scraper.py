from scraper import Scraper

class AnimeScraper(Scraper):
    BASE_URL = 'https://onepiece.fandom.com/wiki/Episode_'
    DIRECTORY = 'AnimeEpisodes'

    def __init__(self, base_url, episode_count):
        super().__init__(base_url, episode_count)
    
    def get_characters(self, soup):
        char_section_title = soup.find('span', id = 'Characters_in_Order_of_Appearance')
        characters = []

        if char_section_title:
            char_list = char_section_title.find_next('ul').find_all('li')
            characters = [li.text.strip() for li in char_list]
        
        return characters

def main():
    scraper = AnimeScraper(AnimeScraper.BASE_URL, 1)
    scraper.scrape(AnimeScraper.DIRECTORY)

if __name__ == "__main__":
    main()