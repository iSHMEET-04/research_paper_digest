from agents.discovery import fetch_papers
from agents.filter import filter_papers
papers= fetch_papers()
print(papers[0])

filtered = filter_papers(papers)

print(len(filtered))