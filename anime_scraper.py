from bs4 import BeautifulSoup
import requests
import json

class AnimeScraper:
    BASE_URL = 'https://onepiece.fandom.com/wiki/Episode_'

    def __init__(self, base_url, episode_count):
        self.base_url = base_url
        self.episode_count = episode_count
        self.episode_urls = self.get_episode_urls()
    
    def get_episode_urls(self):
        return [f'{self.base_url}{i}' for i in range(1, self.episode_count + 1)]
    
    def get_page_content(self, url):
        page = requests.get(url).text
        return BeautifulSoup(page, 'lxml')

    def get_episode_title(self, soup):
        return soup.find('h2', class_ = 'pi-item pi-item-spacing pi-title pi-secondary-background').text

    def get_episode_num(self, soup):
        return soup.find('span', 'mw-page-title-main').text

    def get_short_summary(self, soup):
        return soup.find('span', id = 'Short_Summary').find_next('p').text

    def get_long_summary(self, soup):
        long_summary = ""

        long_heading = soup.find('span', id = 'Long_Summary')
        contents_after = long_heading.parent.find_next_siblings('p')

        for paragraph in contents_after:
            long_summary += paragraph.text

        return long_summary
    
    def get_characters(self, soup):
        char_section_title = soup.find('span', id = 'Characters_in_Order_of_Appearance')
        characters = []

        if char_section_title:
            char_list = char_section_title.find_next('ul').find_all('li')
            characters = [li.text.strip() for li in char_list]
        
        return characters
    
    def scrape(self):
        for url in self.episode_urls:
            page_content = self.get_page_content(url)

            title = self.get_episode_title(page_content)
            episode_number = self.get_episode_num(page_content)
            short_summary = self.get_short_summary(page_content)
            long_summary = self.get_long_summary(page_content)
            characters = self.get_characters(page_content)


            episode_data = {
                'chapter_number': episode_number,
                'title': title,
                'short_summary': short_summary,
                'long_summary': long_summary,
                'characters': characters

            }

            with open(f'AnimeEpisodes/one_piece_episode_{episode_number}.json', 'w') as f:
                json.dump(episode_data, f, indent = 2)
    
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

def main():
    scraper = AnimeScraper(AnimeScraper.BASE_URL, 1)
    scraper.scrape()

if __name__ == "__main__":
    main()

    