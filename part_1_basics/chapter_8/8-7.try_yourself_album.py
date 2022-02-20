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
