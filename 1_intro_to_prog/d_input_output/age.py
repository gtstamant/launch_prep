# Ask user for age
age = int(input('How old are you? '))

#Print users current age
print(f'You are {age} years old.')

#Calculate future ages and print
years = [x * 10 for x in range(1, 5)]
for year in years:
    print(f'In {year} years, you will be {age + year} ' 
          f'years old.')
