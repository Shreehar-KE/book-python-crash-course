"""
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() that prints each text message and
moves each message to a new list called sent_messages as it's printed. After
calling the function, print both of your lists to make sure the messages were
moved correctly.
"""


def show_messages(messages_list):
    """prints the messages in the list"""
    for message in messages_list:
        print(message)


def send_messages(messages_list, sent_messages):
    """simulates sending the messages in the list"""
    while messages_list:
        message = messages_list.pop(0)
        sent_messages.append(message)
        print(f'Sending---> {message}')

    print('\nFinished sending messages...')


messages = ['This is a message',
            'This is also a message',
            'This is another message',
            'This is the last message'
            ]
sent_messages = []
send_messages(messages, sent_messages)

print('\nMessages in List:')
show_messages(messages)
print('\nSent Messages:')
show_messages(sent_messages)
