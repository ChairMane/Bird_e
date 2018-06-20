import requests
import json
import time

config = json.load(open('config.json'))

class Bird_e:

    def get_recent_observation(self, regional_code, maxResults=None, back=None):

        eBird_key = config['ebird_token']
        final_url_obs = 'https://ebird.org/ws2.0/data/obs/' + regional_code + '/recent/?'
        if maxResults:
            final_url_obs += 'maxResults=' + maxResults + '&'
        if back:
            final_url_obs += 'back=' + back + '&'
        final_url_obs += 'key=' + eBird_key
        print(final_url_obs)
        obs = requests.get(final_url_obs)
        observations = obs.json()
        for dict in observations:
            print(dict["comName"])

    def get_recent_notable_observation(self, regional_code, maxResults='', back=''):

        eBird_key = config['ebird_token']
        final_url_obs = 'https://ebird.org/ws2.0/data/obs/' + regional_code + '/recent/notable/?'
        if maxResults:
            final_url_obs += 'maxResults=' + maxResults + '&'
        if back:
            final_url_obs += 'back=' + back + '&'
        final_url_obs += 'key=' + eBird_key
        print(final_url_obs)
        obs = requests.get(final_url_obs)
        observations = obs.json()
        for dict in observations:
            print(dict["comName"])


bird = Bird_e()

regional_code = input("Enter regional code here: ")
maxresults = input("Enter max results: ")
back = input("Enter how far back you want to go: ")
'''bird.get_recent_observation(regional_code, maxresults, back)
print("Below is recent notable observations: ")
bird.get_recent_notable_observation(regional_code, maxresults, back)'''