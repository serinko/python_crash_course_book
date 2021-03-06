def make_album(artist, title, year=None, label=''):
    album = {
        'artist': artist,
        'title': title,
    }

    if year:
        album['year'] = year
    if label:
        album['label'] = label

    return album


albums = []

print("\nWelcome to your music archive. Please enter a new album.")
print("Note that 'artist' and 'album' are mandatory fields, "
      "the rest is optional: ")

while True:

    print("(enter 'q' at any time to quit)\n")

    artist_name = input("Artist name: ")
    if artist_name.lower() == 'q':
        break
    album_title = input("Album title: ")
    if album_title.lower() == 'q':
        break
    year_release = input("Year of release: ")
    if year_release.lower() == 'q':
        break
    label = input("Label: ")
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
print("\nThank you for using our library, have a good listening time")
print("Your albums: ")
for album in albums:
    print("\n")
    for key, value in album.items():
        value = str(value)
        print(f"{key.title()}: {value.title()}")
