"""
8-9. Messages: Make a list containing a series of short text messages. Pass the
list to a function called show_messages(), which prints each text message.
"""


def show_messages(messages_list):
    """prints the messages in the list"""
    for message in messages_list:
        print(message)


messages = ['This is a message',
            'This is also a message',
            'This is another message',
            'This is the last message'
            ]

show_messages(messages)
