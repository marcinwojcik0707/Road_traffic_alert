from requests import get
from os import environ
from dotenv import load_dotenv

class DistanceMatrix:
    def __init__(self, origins, destination, departure_time='now'):
        self.body = self._get_body_data_from_api(origins, destination, departure_time)
    def _get_body_data_from_api(self, origins, destiination, departure_time):
        load_dotenv()
        api_key = environ.get('API_KEY')
        url = 'https://maps.googleapis.com/maps/api/distancematrix/json'
        payload = {
            'origins': origins,
            'destinations': destiination,
            'departure_time': departure_time,
            'key': api_key
        }
        response = get(url, payload)
        print(response.url)
        return response.json()
    def distance_of_road_in_km(self):
        distance_in_metres = self.body['rows'][0]['elements'][0]['distance']['value']
        return int(distance_in_metres)/1000
    def duration_of_road_in_minutes(self):
        duration_in_seconds = self.body['rows'][0]['elements'][0]['duration_in_traffic']['value']
        return round(int(duration_in_seconds)/60)



