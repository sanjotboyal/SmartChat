import urllib.request
import json
from pprint import pprint
import ast

def sentiment(input_content):
  url = "https://eastus.api.cognitive.microsoft.com/text/analytics/v2.1/sentiment?"

  # with open(input_content) as f:
  #     content = f.read() # reads the content from sample.txt
  #     # content = content.replace("\n","")
  #     # print(content)

  values = {
      "documents": [
        {
          "countryHint": "US",
          "id": "1",
          "text": input_content
        }
      ]
    }

  headers = {
      "Content-Type": "application/json",
      "Accept": "application/json",
      'Ocp-Apim-Subscription-Key': '160923276c3b48e6a0215dac9b54e152'
      }

  data = json.dumps(values).encode("utf-8")

  try:
      req = urllib.request.Request(url, data, headers)
      with urllib.request.urlopen(req) as f:
          res = f.read()
      return ast.literal_eval(res.decode())["documents"][0]["score"]
  except Exception as e:
      return e

