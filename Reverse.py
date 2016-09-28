#Sarah Villegas
#Tuesday, Sept. 27, 2016
import requests
import json

#Remove TOKEN before git committing
keys ={"token":"", "github": "https://github.com/aceLeVillegas/Code2040Challenge"}

#send a request to retrieve the word I need
word = requests.post("http://challenge.code2040.org/api/reverse", keys )

#print(word.text)
# Used a extended splice to reverse the word given
backwards = word.text[::-1]
#print(backwards)

#New key containing the reversed word
#Remove TOKEN before git committing
sendKey = {"token": "", "string": backwards}

# Sends back string reversed
reverse = requests.post("http://challenge.code2040.org/api/reverse/validate", sendKey)


print(reverse.text)
