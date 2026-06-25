from pydantic import BaseModel

class PaperAnalysis(BaseModel):
    summary: str
    novelty:str
    engineering_takeaway: str



from groq import Groq
import os

import os
from groq import Groq

def get_client():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment")

    return Groq(api_key=api_key)

def analyze_paper(paper):

    client= get_client()
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