def read_file(filename):
    """Count the approximate number of words in a file"""

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file  {filename} does not exist")

    else:
        print(contents)


filenames = ['dogs.txt', 'cats.txt']
read_file(filenames[0])
print("\n\n")
read_file(filenames[1])
