import requests

def summarize(content):
    r = requests.post(
    "https://api.deepai.org/api/summarization",
    files={
        'text':content,
    },
    headers={'api-key': '2080747b-b6f5-45a2-8f76-b919ebff180b'}
    )
    return r.json()["output"]

