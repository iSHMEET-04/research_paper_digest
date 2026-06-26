# Research Paper Digest Agent
An automated agentic AI system that continuously fetches, filters, and analyzes the latest machine learning research papers from arXiv and generates structured daily intelligence reports using GitHub Actions.

## Overview
This project builds a lightweight autonomous research intelligence pipeline that runs fully without user input.

Every run:

- Fetches latest AI/ML papers from arXiv
- Filters papers based on relevance to LLMs, agents, RAG, reasoning, etc.
- Uses a Groq LLM to analyze selected papers
- Generates structured markdown reports
- Commits results back to the repository

## System Architecture
GitHub Actions (Scheduled Trigger)
Paper Discovery Agent (arXiv API)
Filtering Agent (keyword-based relevance filter)
Analysis Agent (Groq LLM)
Report Generator
GitHub Repository (output/reports)

## Tech Stack
- Python 3.12  
- arXiv API (feedparser)  
- Groq LLM (LLaMA 3 models)  
- GitHub Actions (CI/CD automation)  
- Markdown reporting  
- Pydantic (structured data handling)

## How It Works

### 1. Paper Discovery
Fetches the latest papers from arXiv using RSS feeds:

- cs.AI  
- cs.LG  
- cs.CL  
- cs.CV

### 2. Filtering Layer
Papers are filtered using keyword matching:

- agent  
- RAG  
- LLM  
- reasoning  
- multimodal  
- fine-tuning
Only relevant papers are passed forward.

### 3. LLM Analysis (Groq)
Each paper is analyzed using a large language model.
The model extracts:
- Summary  
- Novelty  
- Engineering Takeaways

### 4. Report Generation
A structured markdown report is created:
- One section per paper  
- Clear headings  
- Stored in `output/reports/`

### 5. Automation via GitHub Actions
The pipeline runs automatically using GitHub Actions:
- Scheduled daily execution  
- Manual trigger via workflow dispatch

### GitHub Actions (Automation)
The entire pipeline is automated using GitHub Actions. The workflow runs on a scheduled trigger (once per day) and can also be manually triggered for testing.

On each run, GitHub Actions:

- Sets up a clean Python environment
- Installs project dependencies
- Injects the Groq API key securely using repository secrets
- Executes the full research pipeline
- Generates a markdown report from latest arXiv papers
- Commits the output report back to the repository if changes exist
This ensures the system runs continuously without manual intervention and maintains a historical log of daily research insights.
