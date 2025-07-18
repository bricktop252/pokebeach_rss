from flask import Flask, Response
from feedgen.feed import FeedGenerator
from scraper import scrape_pokebeach

app = Flask(__name__)

@app.route("/rss")
def generate_rss():
    items = scrape_pokebeach()
    fg = FeedGenerator()
    fg.title("PokéBeach News")
    fg.link(href="https://www.pokebeach.com/", rel="alternate")
    fg.description("Latest news scraped from PokéBeach")

    for item in items:
        entry = fg.add_entry()
        entry.title(item["title"])
        entry.link(href=item["link"])
        if item["pubDate"]:
            entry.pubDate(item["pubDate"])

    return Response(fg.rss_str(pretty=True), mimetype='application/rss+xml')

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))  # Default fallback
    app.run(host="0.0.0.0", port=port)
