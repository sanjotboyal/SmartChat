import requests  
import json
from .cog_ser_test import sentiment

def summarize(content):
    r = requests.post(
    "https://api.deepai.org/api/summarization",
    files={
        'text':content,
    },
    headers={'api-key': '2080747b-b6f5-45a2-8f76-b919ebff180b'}
    )
    sentiment_rating = sentiment(r.json()["output"])

    output_json_data = {"sentiment": sentiment_rating, "summary_text": r.json()["output"]}
    output_json = json.dumps(output_json_data)
    
    return output_json
