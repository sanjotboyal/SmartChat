import requests

r = requests.post(
    "https://api.deepai.org/api/summarization",
    files={
        'text': open('sample.txt', 'rb'),
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)
print(r.json())