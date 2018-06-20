import requests
import json
import time

config = json.load(open('config.json'))

'''eBird_key = config['ebird_token']
observations = []

url_obs = 'https://ebird.org/ws2.0/data/obs/'
regional_code = input("Enter regional code here: ")

final_url_obs = url_obs + regional_code + "/recent/notable/?back=30&maxResults=10&key=" + eBird_key


print(final_url_obs)

obs = requests.get(final_url_obs)

observations = obs.json()
for dict in observations:
    print(dict["comName"])'''

class Bird_e:

    def get_recent_observation(self, regional_code, maxResults=None, back=None):

        eBird_key = config['ebird_token']
        url_obs = 'https://ebird.org/ws2.0/data/obs/'
        if maxResults:
            final_url_obs = url_obs + "/recent/?"
        #final_url_obs = url_obs + regional_code + "/recent/notable/?back=30&maxResults=10&key=" + eBird_key
        print(final_url_obs)
        obs = requests.get(final_url_obs)
        observations = obs.json()
        for dict in observations:
            print(dict["comName"])

    def get_recent_notable_observation(self, regional_code, maxResults='', back=''):

        eBird_key = config['ebird_token']
        url_obs = 'https://ebird.org/ws2.0/data/obs/'
        if maxResults != '' and back != '':
            final_url_obs = url_obs + regional_code + "/recent/notable/?back=" + back + "&maxResults=" + maxResults + "&key=" + eBird_key
        elif maxResults == '' and back != '':
            final_url_obs = url_obs + regional_code + "/recent/notable/?back=" + back + "&key=" + eBird_key
        elif maxResults != '' and back == '':
            final_url_obs = url_obs + regional_code + "/recent/notable/?maxResults=" + maxResults + "&key=" + eBird_key
        else:
            final_url_obs = url_obs + regional_code + "/recent/notable/?key=" + eBird_key
        # final_url_obs = url_obs + regional_code + "/recent/notable/?back=30&maxResults=10&key=" + eBird_key
        print(final_url_obs)
        obs = requests.get(final_url_obs)
        observations = obs.json()
        for dict in observations:
            print(dict["comName"])


bird = Bird_e()

regional_code = input("Enter regional code here: ")
maxresults = input("Enter max results: ")
back = input("Enter how far back you want to go: ")
bird.get_recent_observation(regional_code, maxresults, back)