import requests
import json
import time

config = json.load(open('config.json'))

class Bird_e:

    #Grabs recent observations within a local ID. regiona codes accepted:
    #subnational1, subnational2, eBird local ID or country code.
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

    #Grabs recent notabel observations within a local ID. regiona codes accepted:
    #subnational1, subnational2, eBird local ID or country code.
    def get_recent_notable_observation(self, regional_code, maxResults=None, back=None):

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

    #Grabs species that were recently observed.
    #speciesCodes are six letters long, and usually use first three letters of first name
    #then first three of second name. If the bird just has one name, it's the first six letters.
    #If a bird has more than two names, then you must make up six letters from those names.
    def get_recent_species_observation(self, regional_code, speciesCode, maxResults=None, back=None):

        eBird_key = config['ebird_token']
        final_url_obs = 'https://ebird.org/ws2.0/data/obs/' + regional_code + '/recent/' + speciesCode + '?'
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
speciescode = input("Enter species code: ")
maxresults = input("Enter max results: ")
back = input("Enter how far back you want to go: ")
bird.get_recent_species_observation(regional_code, speciescode, maxresults, back)
'''bird.get_recent_observation(regional_code, maxresults, back)
print("Below is recent notable observations: ")
bird.get_recent_notable_observation(regional_code, maxresults, back)'''