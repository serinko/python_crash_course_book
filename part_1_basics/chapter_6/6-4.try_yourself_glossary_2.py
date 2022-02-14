programming_glossary = {
    'print()': 'Prints a string.',
    'append()': 'Add a value to the list.',
    'del ': 'Permanently removes an item.',
    'for loop': 'For each item - do action.',
    'if-else': 'Statement choosing of two possibilities.',
    'set()': 'returns a set of unique values',
    'items()': 'returns key-value pairs from a dictionary',
    'keys()': 'returns all keys from a dictionary',
    'values()': 'returns all the values froma dictionary',
    'title()': 'a method returning a string starting with a capitol letter'
}

print("Glossary of programming words:")

for word, meaning in sorted(programming_glossary.items()):
    print(f"\t- {word}: {meaning.title()}")
