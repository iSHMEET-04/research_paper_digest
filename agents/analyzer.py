from pydantic import BaseModel

class PaperAnalysis(BaseModel):
    summary: str
    novelty:str
    engineering_takeaway: str



from groq import Groq
import os

client= Groq(
    api_key= os.getenv("GROQ_API_KEY")
)

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

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{
            "role": "user",
            "content": prompt
        }],
        temperature=0.2,
        max_tokens=1000
    )
    return response.choices[0].message.content