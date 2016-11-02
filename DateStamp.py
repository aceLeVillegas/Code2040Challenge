#Sarah Villegas
#Tuesday Nov. 1 2016
import requests
import json
import datetime

#Remove TOKEN before git committing
keys = {"token": "", "github": "https://github.com/aceLeVillegas/Code2040Challenge"}

#sends a request to retrieve the dictionary
dict = requests.post("http://challenge.code2040.org/api/dating", keys)

print(dict.text)

#Makes the response post to a json dictionary
pullApart = json.loads(dict.text)

#format needed for ISO 6801
format = "%Y-%m-%dT%H:%M:%SZ"

#Seperate datestamp and interval
date = pullApart["datestamp"]
time = pullApart["interval"]

#This will clean up the format so I can work with the datetime object
days = datetime.datetime.strptime(date, format)
#print(days)

#Adding the interval with the original date
tick = datetime.timedelta(seconds= time) + days
#print(tick)

#Converts the datetime objects back into the ISO 8601 format
timestamp = tick.isoformat() + "Z"
#print(timestamp)

#Remove TOKEN before git committing
answerKey = {"token": "", "datestamp": timestamp}

answer = requests.post("http://challenge.code2040.org/api/dating/validate", json= answerKey)

print(answer.text)
