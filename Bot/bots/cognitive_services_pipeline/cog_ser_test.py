import urllib.request
import json
from pprint import pprint

url = "https://eastus.api.cognitive.microsoft.com/text/analytics/v2.1/keyphrases?"

with open("sample.txt") as f:
    content = f.read() # reads the content from sample.txt

values = {
    "documents": [
      {
        "countryHint": "US",
        "id": "1",
        "text": content
      }
    ]
  }

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    'Ocp-Apim-Subscription-Key': '160923276c3b48e6a0215dac9b54e152'
    }

data = json.dumps(values).encode("utf-8")
pprint(data)

try:
    req = urllib.request.Request(url, data, headers)
    with urllib.request.urlopen(req) as f:
        res = f.read()
    pprint(res.decode())
except Exception as e:
    pprint(e)