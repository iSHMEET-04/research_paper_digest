import feedparser

def fetch_papers():
    url= (
        "http://export.arxiv.org/api/query?"
        "search_query=cat:cs.AI"
        "&start=0"
        "&max_results=20"
        "&sortBy=submittedDate"
        "&sortOrder=descending"
    )
    feed= feedparser.parse(url)
    papers=[]
    for entry in feed.entries:
        papers.append({
            "title": entry.title,
            "summary": entry.summary,
            "published": entry.published,
            "link": entry.link
        })
    return papers