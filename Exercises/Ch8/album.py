"""
8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a value for
the number of songs, add that value to the album's dictionary. Make at least
one new function call that includes the number of songs on an album.
"""


def make_album(artist, album, songs_count=None):
    """returns a dictionary containing the artist's name and album's name"""
    music_album = {'artist': artist, 'album': album}
    if songs_count:
        music_album['songs_count'] = songs_count
    return music_album


print(f'\n{make_album("Bob Dylan","Highway 61 Revisited")}')
print(f'\n{make_album("Billy Joel","Storm Front",10)}')
print(f'\n{make_album("John Lennon","Imagine")}')
