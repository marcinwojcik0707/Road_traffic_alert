from requests import get
from os import environ
from dotenv import load_dotenv
import main
from send_notification import send_telegram_message, send_email

class DistanceMatrix:
    """Class which connect with distancematrix api and get data about specified route
    """    
    def __init__(self, origins, destination, departure_time='now'):
        """ Create object attribute - api response body.

        Args:
            origins (str): route starting point
            destination (str): route destintation
            departure_time (str, optional): time of route departure. Defaults to 'now'.
        """        
        self.body = self._get_body_data_from_api(origins, destination, departure_time)
    def _get_body_data_from_api(self, origins, destination, departure_time):
        """Request to a distancematrix api.

        Args:
            origins (str): route starting point
            destination (str): route destintation
            departure_time (str, optional): time of route departure. Defaults to 'now'.

        Returns:
            JSON : json object containing response from api
        """        
        load_dotenv()
        api_key = environ.get('API_KEY_MAPS')
        url = 'https://maps.googleapis.com/maps/api/distancematrix/json'
        payload = {
            'origins': origins,
            'destinations': destination,
            'departure_time': departure_time,
            'key': api_key
        }
        response = get(url, payload)
        return response.json()
    def distance_of_route_in_km(self):
        """Filter route distance from api response

        Returns:
            int: route distance in km
        """        
        distance_in_metres = self.body['rows'][0]['elements'][0]['distance']['value']
        return int(distance_in_metres)/1000
    def duration_of_route_in_minutes(self):
        """Filter route duration from api response

        Returns:
            int: route duration in minutes
        """        
        duration_in_seconds = self.body['rows'][0]['elements'][0]['duration_in_traffic']['value']
        return round(int(duration_in_seconds)/60)

def route_traffic_checking(origins, destination, normal_time_of_travel):
    """If actual time route longer than normal time, send email and telegram allert.

    Args:
        origins (str): road starting point
        destination (str): road destintation
        normal_time_of_travel (int): maximum travel time when traffic allert will not send

    Returns:
        CancelJob: Cancel current job in schedule module
    """    
    my_road = DistanceMatrix(origins, destination)
    if my_road.duration_of_route_in_minutes() > int(normal_time_of_travel):
        subject = 'Traffic alert!'
        message = f'Look out!\nTravel from:{origins}\nto:{destination}\nlonger than usual.\nRoad to go: {my_road.distance_of_route_in_km()} km.\nTravel time with current traffic volume: {my_road.duration_of_route_in_minutes()} min.'
        send_telegram_message(message)
        send_email(message, subject)
    return main.schedule.CancelJob



