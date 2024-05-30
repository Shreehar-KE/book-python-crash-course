"""
8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album's artist and title. Once you have that
information, call make_album() with the user's input and print the dictionary
that's created. Be sure to include a quit value in the while loop.
"""


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
