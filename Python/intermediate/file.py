liked_songs = {
    'Lagi' : 'BINI',
    'Eba' : 'Kiyo',
    'Dilaw' : 'Maki'
}

def write_liked_songs_to_file(liked_songs, file_name):
    with open(file_name, 'w') as src:
        src.write('Liked Songs:\n')
        for k,v in liked_songs.items():
            src.write(f'{k} by {v}\n')


if __name__ == '__main__':
    write_liked_songs_to_file(liked_songs, "liked_songs.txt")
