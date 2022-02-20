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

while True:
    print("\nHello, do you want to add an album, press a key and enter")
    print("(enter 'q' at any time to quit)")

    artist_name = input("Album name :")
    if artist_name.lower() == 'q':
        break
    album_title = input("Album title :")
    if album_title.lower() == 'q':
        break
    year_release = input("Year of release: ")
    if year_release.lower() == 'q':
        break
    label = input("Label : ")
    if label.lower() == 'q':
        break

    formatted_album = make_album(
        artist_name,
        album_title,
        year_release,
        label,
    )
    albums.append(formatted_album)

    print("\nWould you like to add another album to your library? ")
    no = input("(enter any key to continue, or 'q' to quit.)")

    if no == 'q':
        break

print("\n\n\n ========================================================= ")
print("Thank you for using our library, have a good listening time")
print("Your albums: ")
for album in albums:
    print("\n")
    for key, value in album.items():
        value = str(value)
        print(f"{key.title()}: {value.title()}")