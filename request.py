import requests
import json

keys ={"token":"", "github": "https://github.com/aceLeVillegas/Code2040Challenge"}

response = requests.post("http://challenge.code2040.org/api/register", keys )

print(response.text)
