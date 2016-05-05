phrase = 'mackerel'
file = 'tube_stations.txt'

stations = [] # list of matching stations
with open(file, 'r') as f:
    next(f) # skip the header line
    for station in f:
        if not any(letter in station.lower() for letter in phrase.lower()):
            stations.append(station.rstrip())

print('{} has {} matching station(s) ({})'.format(phrase, len(stations), ', '.join(stations)))