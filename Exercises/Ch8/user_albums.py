def make_album(artist, album):
    """returns a dictionary containing the artist's name and album's name"""
    music_album = {'artist': artist, 'album': album}
    return music_album


while True:
    print('\nEnter your favorite music album:')
    print("(Enter 'q' to quit at anytime)\n")

    artist = input('Artist Name: ')
    if artist == 'q':
        break
    album = input('Album Name: ')
    if album == 'q':
        break
    print(f'\n{make_album(artist,album)}')
