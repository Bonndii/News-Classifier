import feedparser 
from trafilatura import fetch_url, extract

rss_url = "http://tass.com/rss/v2.xml"

def extract_article_text(url: str) -> str | None:
    downloaded = fetch_url(url)

    text = extract(downloaded, output_format="txt", include_comments=False, include_tables=False, favor_precision=True)

    return text

def fetch_feed_items(url):
    feed = feedparser.parse(url)
    items = []
    for entry in feed.entries[:99]:
        items.append({
            "title": entry.title,
            "link": entry.link,
            "publication_date": entry.published
        })
    return items