from agents.discovery import fetch_papers
from agents.filter import filter_papers
from agents.analyzer import analyze_paper
from agents.report import generate_report
from datetime import datetime
papers= fetch_papers()
papers= filter_papers(papers)

results=[]

for paper in papers[:5]:

    analysis = analyze_paper(
        paper
    )
    results.append(
        {
            "title": paper["title"],
            "analysis": analysis,
        }
    )

report= generate_report(results)
print(report)
today= datetime.now().strftime("%Y-%m-%d")
output_file= f"output/reports/report_{today}.md"
with open(
    output_file,
    "w",
    encoding="utf-8",
) as f:
    f.write(report)
