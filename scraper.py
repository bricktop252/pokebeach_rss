import requests
from bs4 import BeautifulSoup

def scrape_pokebeach():
    url = "https://www.pokebeach.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    items = []
    for article in soup.select('div.home-news-post'):
        title_tag = article.select_one('h2 a')
        if not title_tag:
            continue
        title = title_tag.get_text(strip=True)
        link = title_tag['href']
        date_tag = article.select_one('span.post-date')
        pubDate = date_tag.get_text(strip=True) if date_tag else None

        items.append({
            'title': title,
            'link': link,
            'pubDate': pubDate,
        })
    return items
