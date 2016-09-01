import requests
import json

keys ={"token":"c7e21aa496fe24dfc7fc0a9cd21627ef", "github": "https://github.com/aceLeVillegas/Code2040Challenge"}

response = requests.post("http://challenge.code2040.org/api/register", keys )

print(response.text)
