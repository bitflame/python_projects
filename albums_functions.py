def make_album(artist, title, songs=None):
    result = {
        'artist': artist,
        'album_title': title,
        'number_of_songs': songs,
    }
    return result