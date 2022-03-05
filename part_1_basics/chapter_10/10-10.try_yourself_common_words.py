def count_words(filename, word):
    """Count the number of a word appereance in a text"""

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file  {filename} does not exist")
        # Commented so we pass silently
        # pass

    else:

        my_word = word
        word_count = contents.lower().count(my_word)
        print(f"The word {my_word} appears {word_count} times in"
              f" the file {filename}.")


filenames = [
    "Alice in Wonderland.txt", 'siddhartha.txt', 'moby_dick.txt',
    'harry_potter.txt']
#
# count_words(filenames[0], 'mountain')
# count_words(filenames[1], 'death')
# count_words(filenames[2], 'whale')
# count_words(filenames[3], 'Harry')

for filename in filenames:
    word = 'dark'
    count_words(filename, word)
