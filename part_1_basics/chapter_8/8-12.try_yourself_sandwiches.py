def sendwich_fillings(*args):
    """Displays a simple summary of a sandwich fillings"""
    print("\nThese fillings will be added to your sendwich:")
    if args:
        for arg in args:
            print(f"\t- {arg}")
    else:
        print("\t- no fillings chosen")


sendwich_fillings('ham', 'cheese', 'butter')
sendwich_fillings('butter', 'jam')
sendwich_fillings('peanut butter', 'chilli', 'bacon', 'anchovy')
sendwich_fillings()
