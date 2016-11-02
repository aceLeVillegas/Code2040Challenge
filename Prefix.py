#Sarah Villegas
#Tuesday Nov. 1 2016
import requests
import json

#Remove TOKEN before git committing
keys = {"token": "", "github": "https://github.com/aceLeVillegas/Code2040Challenge"}

#sends a request to retrieve the dictionary
search = requests.post("http://challenge.code2040.org/api/prefix", keys)

print(search.text)

#Makes the texts into a json dictionary
dict = json.loads(search.text)

#This seperates the prefix and array given by the API
prefix = dict["prefix"]
arra = dict["array"]

#This will contain all the words that do not start with the prefix
found = []

#goes through arra to find if the prefix is within the array given
for i in range(len(arra)):

    if(arra[i].find(prefix) != 0):

        found.append(arra[i])

print(found)

#Create the key that contains the new array and the token
answerKey = {"token": "", "array": found}

#Sends to the API the answerKey
#Since I had a seperated it in a JSON dictionary needed to return it to the API as a JSON object
answer = requests.post("http://challenge.code2040.org/api/prefix/validate", json =answerKey)

print(answer.text)
