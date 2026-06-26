from pydantic import BaseModel
from agents.llm import llm
from langsmith import traceable
from dotenv import load_dotenv
load_dotenv()

class PaperAnalysis(BaseModel):
    summary: str
    novelty:str
    engineering_takeaway: str

@traceable(name='Paper Analysis')
def analyze_paper(paper):
    prompt = f"""
    Analyze the following paper.

    Return:

    1. Summary
    2. Novelty
    3. Engineering Takeaway

    Paper:

    {paper['summary']}
    """

    response = llm.invoke(prompt)
    return response.content