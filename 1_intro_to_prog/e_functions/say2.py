def say(text='hello'):
    print(f'{text}!')

greetings = ['hello',
             'hi',
             'how do you do',
             'Quite all right',
]

say()

for greeting in greetings:
    say(greeting)