import re
import webbrowser
from urllib.parse import quote_plus

def open_url(url):
    if not re.match(r"^https?://", url):
        url = "https://" + url
    webbrowser.open(url)
    return f"Opening {url}."

def google_search(query):
    webbrowser.open("https://www.google.com/search?q=" + quote_plus(query))
    return f"Searching Google for {query}."

def youtube_search(query):
    webbrowser.open("https://www.youtube.com/results?search_query=" + quote_plus(query))
    return f"Searching YouTube for {query}."

def web_search(query, max_results=5):
    try:
        from ddgs import DDGS
        results = DDGS().text(query, max_results=max_results)
        clean = []
        for r in results:
            clean.append({
                "title": r.get("title",""),
                "body": r.get("body",""),
                "href": r.get("href","")
            })
        return clean
    except Exception:
        return []
