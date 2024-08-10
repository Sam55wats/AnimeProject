from manga_scraper import MangaScraper
import pytest
from bs4 import BeautifulSoup

@pytest.fixture
def mock_scraper():
    return MangaScraper(MangaScraper.BASE_URL, 3)

def test_get_chapter_urls():
    scraper = MangaScraper(MangaScraper.BASE_URL, 3)
    assert scraper.get_num_chapters() == 3

def test_get_chapter_title():
    scraper = MangaScraper(MangaScraper.BASE_URL, 2)
    page_content = scraper.get_page_content(scraper.chapter_urls[0])
    assert scraper.get_chapter_title(page_content) == "Romance Dawn - The Dawn of the Adventure"

def test_get_chapter_num():
    scraper = MangaScraper(MangaScraper.BASE_URL, 2)
    page_content = scraper.get_page_content(scraper.chapter_urls[0])
    assert scraper.get_chapter_num(page_content) == "Chapter 1"

def test_get_short_sum():
    scraper = MangaScraper(MangaScraper.BASE_URL, 2)
    page_content = scraper.get_page_content(scraper.chapter_urls[0])
    assert scraper.get_chapter_num(page_content) == "Chapter 1"

def test_get_characters():
    scraper = MangaScraper(MangaScraper.BASE_URL, 2)
    page_content = scraper.get_page_content(scraper.chapter_urls[0])
    print(scraper.get_characters(page_content))



