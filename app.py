from flask import Flask, Response
from rss import generate_rss_feed  # assuming your rss logic is in rss.py

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>✅ PokéBeach RSS Feed Generator</h2><p>View your feed at <a href='/rss'>/rss</a></p>"

@app.route("/rss")
def rss():
    xml = generate_rss_feed()
    return Response(xml, mimetype='application/rss+xml')

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
