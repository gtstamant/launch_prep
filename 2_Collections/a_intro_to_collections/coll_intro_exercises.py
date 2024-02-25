# How do you determine the number of entries in a list named 'people'?
# people = ['Ben', 'Scott', 'Faizel']
# print(len(people))

stuff = ('hello', 'world', 'bye', 'now')

stuff_list = list(stuff)
stuff_list[2] = 'goodbye'
stuff = tuple(stuff_list)

# print(stuff)

pi = 3.141592
str_pi = str(pi)

# print(type(str_pi))

# print(list(range(3, 17, 4)))

my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# Are theses two lists equal?                       # Yes, elems are same
# Are these two lists the same object?              # No, new obj through constr
# Are the nested lists at index 3 equal?            # Yes, elems are same
# Are the nested lists at index 3 the same object?  # Yes, large list point to same obj

country_map = {
    'Alice':       'USA',
    'Francois':    'Canada',
    'Inti':        'Peru',
    'Monika':      'Germany',
    'Sanyu':       'Uganda',
    'Yoshitaka':   'Japan',
}

def check_country():
    name = input('Provide a name: ')
    country = country_map[name]
    print(f'{name} is associated with {country}.')

check_country()