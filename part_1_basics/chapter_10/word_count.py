# WORKING WITH MULTIPLE FILES

def count_words(filename):
    """Count the approximate number of words in a file"""

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"Sorry, the file  {filename} does not exist")
        # Commented so we pass silently
        pass

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

# FAILING SILENTLY
# pass - tells Python to do nothing and pass the error silently
# We can run the same program just exchange the except block for pass
# The information about harry_potter.txt not existing is not printed

# Pass statement is a placeholder - we tell Python to do nothing
# We can use the information for further work, not shown to the user
