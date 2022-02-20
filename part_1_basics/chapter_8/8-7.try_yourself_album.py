def make_album(artist, title):
    album = {
        'artist': artist,
        'title': title,
    }
    return album


new_album = make_album('nirvana', 'smells like teen spirit')
print(new_album)
new_album = make_album('ellen cox', 'the wolves')
print(new_album)
new_album = make_album('warpaint', 's/t')
print(new_album)


# Add optional argument
def make_album(artist, title, year=None, label=''):
    album = {
        'artist': artist,
        'title': title,
    }

    if year:
        album['year'] = year
    if label:
        pass
    album['label'] = label

    return album


albums = []
album_1 = make_album('nirvana', 'smells like teen spirit', 1991, )
album_2 = make_album('warpaint', 's/t', year=2014, label='rough trade records')
album_3 = make_album('ellen cox', 'the wolves', label='DIY')

albums.append(album_1)
albums.append(album_2)
albums.append(album_3)

for album in albums:
    print(album)

for album in albums:
    print("\n")
    for key, value in album.items():
        value = str(value)
        print(f"{key.title()}: {value.title()}")
