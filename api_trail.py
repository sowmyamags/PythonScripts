#!/usr/bin/env python3

"""import requests
response = requests.get('https://twitter.com/')
print(response)"""

import requests
words = 30
paragraphs = 1
formats = 'text'
response = requests.get(f"https://alexnormand-dino-ipsum.p.rapidapi.com/?format={formats}&words={words}&paragraphs={paragraphs}",
 headers={
   "X-RapidAPI-Host": "alexnormand-dino-ipsum.p.rapidapi.com",
   "X-RapidAPI-Key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
 }
)
print(response.text)

print(type(response.json()))
print(response.json())
