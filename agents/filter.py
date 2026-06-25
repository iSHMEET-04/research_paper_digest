KEYWORDS=[
    "agent",
    "rag",
    "reasoning",
    "AI",
    "llm",
    "language model"
]

def filter_papers(papers):
    filtered=[]
    for paper in papers:
        text=(
            paper["title"]+"\n"
            +paper["summary"]
        ).lower()
        if any(keyword in text for keyword in KEYWORDS):
            filtered.append(paper)
    return filtered

