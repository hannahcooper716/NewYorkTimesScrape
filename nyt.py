import requests
import secrets

# gets stories from a particular section of NY times
#construct our query (base URL, name of section that we want, API key that we have,
#put all together get the json and return it for us)
def get_stories(section):
    baseurl = 'https://api.nytimes.com/svc/topstories/v2/'
    extendedurl = baseurl + section + '.json' #give back top stories from that section
    params={'api-key': secrets.nyt_key}
    return requests.get(extendedurl, params).json()
#when you get back, json with either be a dictionary with a list inside of it or a list,
#each of which is going to be one of the stories/its info

section = 'science'
stories = get_stories(section)
print(stories) # should print a big pile of json

#created secrets to hold our nyt code, imported it into this file, and then instead of nyt_key
#add secrets.nyt_key so that we are getting the key from secrets.py
#no one else can run your program, they will have to create their own secret file with their own API key
