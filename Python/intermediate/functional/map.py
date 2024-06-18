from functools import reduce


# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.8), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

def longer_than_five_minutes(song):
    return song[1] > 5.00

print(list(filter(longer_than_five_minutes, playlist)))

def minutes_to_seconds(song):
    return int(song[1]) * 60 + round((song[1] - int(song[1]))*100)

print(list(map(minutes_to_seconds, playlist)))

def get_durations(song):
    return song[1]

def add_durations(song1, song2):
    return song1 + song2

durations =  list(map(get_durations, playlist))
print(reduce(add_durations, durations))
