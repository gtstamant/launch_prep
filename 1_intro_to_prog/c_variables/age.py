# Calculates and reports future ages

# age = 22
# years = 10

# print(f'You are {age} years old.')
# print(f'In {years} years, you will be {age + years} years old.')
# print(f'In {years * 2} years, you will be {age + (years * 2)} years old.')
# print(f'In {years * 3} years, you will be {age + (years * 3)} years old.')
# print(f'In {years * 4} years, you will be {age + (years * 4)} years old.')

# Better solution

age = 22
years = [x * 10 for x in range(0, 5)]

for year in years:
    if year == 0:
        print(f'You are {age} years old.')
    else:
        age += 10
        print(f'In {year} years, you will be {age} years old.')
