def print_sms(saved_messages):
    """Displays messages saved in the list"""
    print("\nSaved messages:")
    for message in saved_messages:
        print(f"\n{message}")

    print("...")


saved_messages = [
    'Hey what a hot day, you want to go swimming with me',
    'wtf, anotha one wearin crogz in the metro',
    'this must be the end of humans',
    'hahaha, wtf, omg, did he also have socks',
    'wish my handy had a camera, would archive this exot',
    'it became so normal, crogs soks cult',

]

print_sms(saved_messages)
print_sms(saved_messages[:2])
# Prints only first two items from the list
