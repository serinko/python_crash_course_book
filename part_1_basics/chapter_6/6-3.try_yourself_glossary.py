programming_glossary = {
    'print()': 'Prints a string.',
    '.append()': 'Add a value to the list.',
    'del ': 'Permanently removes an item.',
    'for loop': 'For each item - do action.',
    'iif-else': 'Statement choosing of two possibilities.'
}

print('Glossary of programming words:\n')

for word in programming_glossary:
    print(f"{word}:")
    print(f"{str(programming_glossary[word])}")
    print("\n")
