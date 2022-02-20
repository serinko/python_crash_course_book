def make_shirt(size, front_print):
    """Displays T-shirt summary message"""
    print(f"The t-shirt size is: {size.upper()}")
    print(f"The chosen print is: {front_print}")


make_shirt('m', 'a.c.a.b.')
make_shirt(size='m', front_print='a.c.a.b.')
