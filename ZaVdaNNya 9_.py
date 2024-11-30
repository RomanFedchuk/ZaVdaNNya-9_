import requests
from bs4 import BeautifulSoup


def scrape_book_titles(url):
    book_titles = []
    while url:
        print(f"Завантаження сторінки: {url}")
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Помилка {response.status_code}: Неможливо отримати сторінку {url}")
            break

        soup = BeautifulSoup(response.content, 'html.parser')

        for book in soup.find_all('h3'):
            title = book.a['title']
            book_titles.append(title)

        next_page = soup.find('li', class_='next')
        if next_page:
            url = "http://books.toscrape.com/catalogue/" + next_page.a['href']
        else:
            url = None

    return book_titles


if __name__ == "__main__":
    base_url = "http://books.toscrape.com/catalogue/page-1.html"
    titles = scrape_book_titles(base_url)
    print(f"Знайдено {len(titles)} книг:")
    for i, title in enumerate(titles, start=1):
        print(f"{i}. {title}")
