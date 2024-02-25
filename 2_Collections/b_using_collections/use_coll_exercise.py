people_phones = {
    'Chris': '111-2222',
    'Pete':  '333-4444',
    'Clare': '555-6666',
}

# print(people_phones.keys())

# text = ' \t  abc def    \n\r'
# print(text)
# print(repr(text))             # ' \t  abc def    \n\r'
# print(repr(text.strip()))     # 'abc def'

some_range = range(0, 25, 3)
# print(some_range[6])

school_name = 'Launch School'
c_loc = school_name.find('c')
# print(school_name[c_loc:c_loc + 6])

my_tup = (1, 2, 3, 4, 5)
new_tup = my_tup[-2:0:-1]

# print(new_tup)

pets = {
    'Cat': 'Meow',
    'Dog': 'Bark',
    'Bird': 'Tweet',
}

# print(pets.get('Dog'))
# print(pets.get('Lizard'))
# print(pets.get('Lizard', '<silence>'))

# What will the following code print?

# print('abc-def'.isalpha())        # False
# print('abc_def'.isalpha())        # False
# print('abc def'.isalpha())        # False
# print('abc def'.isalpha() and     # False
#       'abc def'.isspace())        
# print('abc def'.isalpha() or      # False
#       'abc def'.isspace())
# print('abcdef'.isalpha())         # True
# print('31415'.isdigit())          # True
# print('-31415'.isdigit())         # False
# print('31_415'.isdigit())         # False
# print('3.1415'.isdigit())         # False
# print(''.isspace())               # False

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
# new_info = info.split(':')
# info = '+'.join(new_info)
info = info.replace(':', '+')
# print(info)

# text = "It's probably pining for the fjords!"

# print(text[21:35].rfind('f'))     # Prints 8; reindexed at slice
# print(text.rfind('f', 21, 35))

stuff = [
    ['hello','world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]

stuff[1][3] = 'new value'
# print(stuff)

cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

# print(cats['Pete']['Cocoa']['enjoys'])

# Determine what each prints

# print('johnson' in 'Joe Johnson')         # False
# print('sen' not in 'Joe Johnson')         # True
# print('Joe J' in 'Joe Johnson')           # True
# print(5 in range(5))                      # False
# print(5 in range(6))                      # True
# print(5 not in range(5, 10))              # False
# print(0 in range(10, 0, -1))              # False
# print(4 in {6, 5, 4, 3, 2, 1})            # True
# print({1, 2, 3} in {1, 2, 3})             # False
# print({3, 2} in {1, frozenset({2, 3})})   # True

numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

def contains_three(collection_list):
    for item in collection_list:
        print(3 in item)

# contains_three(
#     [numbers1,
#      numbers2,
#      numbers3,
#      numbers4,
#      numbers5,
#     ]
# )

# What will each print?

# cats = ('Cocoa', 'Cheddar',
#         'Pudding', 'Butterscotch')
# print('Butterscotch' in cats)         # True
# print('Butter' in cats)               # False
# print('Butter' in cats[3])            # True
# print('cheddar' in cats)              # False

my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

new_tup = zip(my_str, my_list, my_tuple, my_range)
# print(list(new_tup))

# What will be printed by line 10 (= 158)?

# pets = {
#     'Cat':  'Meow',
#     'Dog':  'Bark',
#     'Bird': 'Tweet',
# }

# keys = pets.keys()
# del pets['Dog']
# pets['Snake'] = 'Sssss'
# print(keys)

# Answer: ['Cat', 'Bird', 'Snake']