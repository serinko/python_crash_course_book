def print_saved_sms(saved_messages):
    """Displays messages saved in the list"""
    print("\nSaved messages:")
    for message in saved_messages:
        print(f"\n{message}")

    print("...")


def send_sms(saved_messages, sent_messages):
    """Moves messages from saved messages to sent messages,
    while emptying th original folder."""
    while saved_messages:
        sending_message = saved_messages.pop()
        print(f"\nSending message: {sending_message}")
        sent_messages.append(sending_message)


def print_3_latest_sent_sms(sent_messages):
    """  Displays 3 top sent messages  """
    print("\nSaved messages:")
    for message in sent_messages[:3]:
        print(f"\n{message}")

    print("\n...\n")


saved_messages = [
    'Hey what a hot day, you want to go swimming with me',
    'wtf, anotha one wearin crogz in the metro',
    'this must be the end of humans',
    'hahaha, wtf, omg, did he also have socks',
    'wish my handy had a camera, would archive this exot',
    'it became so normal, crogs soks cult',
]
sent_messages = []
