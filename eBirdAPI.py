import requests
import json
import time
from pprint import pprint

config = json.load(open('config.json'))

class Bird_e:

    #Grabs recent observations within a local ID. regiona codes accepted:
    #subnational1, subnational2, eBird local ID or country code.
    def get_recent_observation(self, regional_code, maxResults=None, back=None):
        sighting = {}
        eBird_key = config['ebird_token']
        final_url_obs = 'https://ebird.org/ws2.0/data/obs/' + regional_code + '/recent/?'
        if maxResults:
            final_url_obs += 'maxResults=' + maxResults + '&'
        if back:
            final_url_obs += 'back=' + back + '&'
        final_url_obs += 'key=' + eBird_key

        obs = requests.get(final_url_obs)
        observations = obs.json()

        for dictionary in observations:
            sighting[dictionary['comName']] = dictionary['locName']

        results = ''
        i = 1
        for key in sighting:
            results += str(i) + '. ' + key + ' seen here: \n' + '     ' + sighting[key] + '\n\n'
            i += 1

        return results

    #Grabs recent notabel observations within a local ID. regiona codes accepted:
    #subnational1, subnational2, eBird local ID or country code.
    def get_recent_notable_observation(self, regional_code, maxResults=None, back=None):
        sighting = {}
        eBird_key = config['ebird_token']
        final_url_obs = 'https://ebird.org/ws2.0/data/obs/' + regional_code + '/recent/notable/?'
        if maxResults:
            final_url_obs += 'maxResults=' + maxResults + '&'
        if back:
            final_url_obs += 'back=' + back + '&'
        final_url_obs += 'key=' + eBird_key

        obs = requests.get(final_url_obs)
        observations = obs.json()

        for dictionary in observations:
            sighting[dictionary['comName']] = dictionary['locName']

        results = ''
        i = 1
        for key in sighting:
            results += str(i) + '. ' + key + ' seen here: \n' + '     ' + sighting[key] + '\n\n'
            i += 1

        return results


    #Grabs species that were recently observed.
    #speciesCodes are six letters long, and usually use first three letters of first name
    #then first three of second name. If the bird just has one name, it's the first six letters.
    #If a bird has more than two names, then you must make up six letters from those names.
    def get_recent_species_observation(self, regional_code, speciesCode, maxResults=None, back=None):
        sighting = []
        eBird_key = config['ebird_token']
        final_url_obs = 'https://ebird.org/ws2.0/data/obs/' + regional_code + '/recent/' + speciesCode + '?'
        if maxResults:
            final_url_obs += 'maxResults=' + maxResults + '&'
        if back:
            final_url_obs += 'back=' + back + '&'
        final_url_obs += 'key=' + eBird_key

        obs = requests.get(final_url_obs)
        observations = obs.json()

        common_name = observations[0]['comName']

        j = 0
        for dictionary in observations:
            sighting.insert(j, dictionary['locName'])
            j+=1

        results = ''

        i = 0
        for index in sighting:
            results += str(i+1) + '. ' + common_name + ' seen here: \n' + '     ' + sighting[i] + '\n\n'
            i += 1

        return results

    #Using latitude and longitude, this function grabs recent observations near
    #the inputted coordinates.
    def get_recent_nearby_observation(self, lat, lng, dist=None, maxResults=None, back=None):
        sighting = {}
        eBird_key = config['ebird_token']
        final_url_obs = 'https://ebird.org/ws2.0/data/obs/geo/recent?lat=' + lat + '&lng=' + lng + '&'
        if dist:
            final_url_obs += 'dist=' + dist + '&'
        if maxResults:
            final_url_obs += 'maxResults=' + maxResults + '&'
        if back:
            final_url_obs += 'back=' + back + '&'
        final_url_obs += 'key=' + eBird_key

        obs = requests.get(final_url_obs)
        observations = obs.json()

        for dictionary in observations:
            sighting[dictionary['comName']] = dictionary['locName']

        results = ''
        i = 1
        for key in sighting:
            results += str(i) + '. ' + key + ' seen here: \n' + '     ' + sighting[key] + '\n\n'
            i += 1

        return results


    def get_recent_species_nearby_observation(self, speciesCode, lat, lng, dist=None, maxResults=None, back=None):

        eBird_key = config['ebird_token']
        final_url_obs = 'https://ebird.org/ws2.0/data/obs/geo/recent/' + speciesCode + '?lat=' + lat + '&lng=' + lng + '&'
        if dist:
            final_url_obs += 'dist=' + dist + '&'
        if maxResults:
            final_url_obs += 'maxResults=' + maxResults + '&'
        if back:
            final_url_obs += 'back=' + back + '&'
        final_url_obs += 'key=' + eBird_key
        print(final_url_obs)
        obs = requests.get(final_url_obs)
        observations = obs.json()
        for dict in observations:
            print(dict['comName'] + ' was found within ' + dist + 'km of your coordinates at ' + dict['locName'] + '.')

