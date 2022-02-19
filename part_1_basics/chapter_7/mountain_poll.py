responses = {}

# set a flag to indicate the polling is active
poling_active = True

while polling_active:
    # Prompt for the persons name and response
    name = input("\n\nWhat is your name? ")
    response = input("\nWhich mountain would you like to climb today? ")

    # Store response in a dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll
    repeat = input("\n\nWould you like to let another person respond?"
                   "(yes/ no)")

    if repeat == 'no':
        polling_active = False

# Polling is complete - show the results
print("\n--- POLL RESULTS ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")
