from langsmith import Client
from langsmith.evaluation import evaluate
from evaluation.target import summarize_paper

client= Client()
def target(inputs):
    return summarize_paper(inputs)
evaluate(
    target,
    data='Research Paper Evaluation',
    experiment_prefix='answer_relevance_v1'
)