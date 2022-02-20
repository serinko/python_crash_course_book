def make_shirt(front_print='I love Python!', size='l'):
    """Displays T-shirt summary message"""
    print(f"The t-shirt size is: {size.upper()}")
    print(f"The chosen print is: {front_print}")


make_shirt()
make_shirt(size='m')
make_shirt(front_print='#ocean', size='xl')
