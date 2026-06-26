from agents.analyzer import analyze_paper


def summarize_paper(inputs: dict) -> dict:
    paper = {
        "title": inputs["title"],
        "summary": inputs["abstract"]
    }
    summary = analyze_paper(paper)
    return {
        "summary": summary
    }