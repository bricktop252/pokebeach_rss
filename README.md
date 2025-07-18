# PokéBeach RSS Feed Generator

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/bricktop252/pokebeach_rss)

This project creates a custom RSS feed from [https://www.pokebeach.com](https://www.pokebeach.com), updated every 6 hours.

## Features
- Scrapes latest articles from PokéBeach
- Generates valid RSS feed
- Flask-based web server
- Auto-refreshes cache every 6 hours

## How to Run Locally

```bash
git clone https://github.com/yourusername/pokebeach_rss.git
cd pokebeach_rss
pip install -r requirements.txt
python app.py
```

Visit: `http://localhost:5000/rss`

## Deploy to Railway

1. Push to GitHub
2. Go to [https://railway.app](https://railway.app)
3. Select your repo
4. Add a Cron job to ping `/rss` every 6 hours

## License

MIT License
