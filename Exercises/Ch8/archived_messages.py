"""
8-11. Archived Messages: Start with your work from Exercise 8-10. Call the func-
tion send_messages() with a copy of the list of messages. After calling the func-
tion, print both of your lists to show that the original list has retained its messages.
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
send_messages(messages[:], sent_messages)

print('\nMessages in List:')
show_messages(messages)
print('\nSent Messages:')
show_messages(sent_messages)
