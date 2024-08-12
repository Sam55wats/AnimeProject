import json
import glob
import os
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

    def character_appearances(directory):
        character_appearances = {}

        for filename in glob.glob(os.path.join(directory, '*.json')):
            with open(filename, 'r') as f:
                data = json.load(f)

                number = data['chapter_number']

                for character in data.get('characters', []):
                    if character not in character_appearances:
                        character_appearances[character] = []
                    character_appearances[character].append(number)
        
        return character_appearances
   

def main():
    scraper = MangaScraper(MangaScraper.BASE_URL, 200)
    scraper.scrape(MangaScraper.DIRECTORY)

if __name__ == "__main__":
    main()
