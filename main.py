from google_maps import DistanceMatrix
if __name__ == '__main__':
    origins = 'Wrocław, Czartoryskiego 17'
    destination = 'Nowa Wieś Wrocławska, Ryszarda Chomicza 13'
    my_road = DistanceMatrix(origins, destination)
    print(my_road.body)
    print(f'Droga do przebycia: {my_road.distance_of_road_in_km()} km.')
    print(f'Czas drogi przy obecnym natężeniu ruchu: {my_road.duration_of_road_in_minutes()} min.')