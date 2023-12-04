def make_album(artist, album):
    """returns a dictionary containing the artist's name and album's name"""
    music_album = {'artist': artist, 'album': album}
    return music_album


print(f'\n{make_album("Bob Dylan","Highway 61 Revisited")}')
print(f'\n{make_album("Billy Joel","Storm Front")}')
print(f'\n{make_album("John Lennon","Imagine")}')
