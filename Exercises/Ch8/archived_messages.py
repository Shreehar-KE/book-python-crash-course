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
        print(sent_messages)

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
