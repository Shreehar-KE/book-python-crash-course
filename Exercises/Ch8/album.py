def make_album(artist, album, songs_count=None):
    """returns a dictionary containing the artist's name and album's name"""
    music_album = {'artist': artist, 'album': album}
    if songs_count:
        music_album['songs_count'] = songs_count
    return music_album


print(f'\n{make_album("Bob Dylan","Highway 61 Revisited")}')
print(f'\n{make_album("Billy Joel","Storm Front",10)}')
print(f'\n{make_album("John Lennon","Imagine")}')
