# WORKING WITH MULTIPLE FILES

def count_words(filename):
    """Count the approximate number of words in a file"""

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file  {filename} does not exist")

    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


# filename = "Alice in Wonderland.txt"
# count_words(filename)
# We use the function and define the argument for its parametter

# Analyzing more texts:
filenames = [
    "Alice in Wonderland.txt", 'siddhartha.txt', 'moby_dick.txt',
    'harry_potter.txt'
]
for filename in filenames:
    count_words(filename)


