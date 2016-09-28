#Sarah Villegas
#Tuesday, Sept. 27, 2016
import requests
import json

#Remove TOKEN before git committing
keys ={"token":"", "github": "https://github.com/aceLeVillegas/Code2040Challenge"}

#send a request to retrieve the word I need
dict = requests.post("http://challenge.code2040.org/api/haystack", keys )

#print(dict.text)

#Makes the texts into a json dictionary
hay = json.loads(dict.text)

#This seperates the needle and haystack given to me by the API
needle = hay['needle']
haystack = hay['haystack']

#looks for the index that contains the value needle holds
needle_index = haystack.index(needle)

#new key created to post to the API
answerKey = {"token" : "", "needle": needle_index}

#Sends the index found
answer = requests.post("http://challenge.code2040.org/api/haystack/validate", answerKey)

#print(hay)

print(answer.text)
#Go through the haystack and compare them to the needle
