prompt = "Hello, how many people are in your dinner group? "
guests = input(prompt)
guests = int(guests)

if guests <= 8:
    print(f"\nYour table will be ready for {str(guests)} people.")
else:
    print(f"\nWe are sorry, but you will have to wait for a table which "
          f"can host {str(guests)} people.")
