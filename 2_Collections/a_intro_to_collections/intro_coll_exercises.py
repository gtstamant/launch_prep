stuff = ('hello', 'world', 'bye', 'now')
stuff_list = list(stuff)
stuff_list[2] = 'goodbye'
stuff = tuple(stuff_list)

print(stuff)

pi = 3.141592
str_pi = str(pi)
print(type(str_pi))

print(list(range(3, 17, 4)))

country_map = {
    'Alice':        'USA',
    'Francois':     'Canada',
    'Inti':         'Peru',
    'Monika':       'Germany',
    'Sanyu':        'Uganda',
    'Yoshitaka':    'Japan',
}

def name_country():
    name = input('Provide a name: ')
    
    while name not in country_map:
        print("Invalid name")
        name = input('Provde another name: ')
    
    return country_map[name]

print(name_country())