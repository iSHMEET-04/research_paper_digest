import json
from langsmith import Client
from dotenv import load_dotenv
import os

load_dotenv()
client = Client()
DATASET_NAME="Research Paper Evaluation"

existing=None
for dataset in client.list_datasets():
    if dataset.name== DATASET_NAME:
        existing= dataset
        break
if existing:
    dataset=existing
else:
    dataset= client.create_dataset(
        dataset_name= DATASET_NAME,
        description= "Dataset for research paper evaluation"
    )
    print(f'Created new dataset: {dataset.name}')

with open("datasets/research_papers.json", "r", encoding="utf-8") as f:
    papers = json.load(f)
for paper in papers:
    client.create_example(
        inputs={
            "title": paper["title"],
            "abstract": paper["abstract"],
        },
        outputs={
            "summary": paper["expected_summary"],
        },
        dataset_id=dataset.id,
    )

print("Dataset upload complete.")