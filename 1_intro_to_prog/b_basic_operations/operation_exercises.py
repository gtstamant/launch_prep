# Concatenate two strings, but here also using interpolation instead
print('Guy ' + 'St. Amant')

first_name = 'Guy'
last_name = 'St. Amant'

print(f'{first_name} {last_name}')

# Extract the digits of 4936

num = 4936

ones = num % 4930
tens = int(((num - 6) / 10) % 490)
hundreds = int(((num - 36) / 100) % 40)
thousands = int(((num - 936) / 1000) % 5)

print(ones, tens, hundreds, thousands)

values = []

while len(values) < 4:
    if len(values) == 0:
        values.append(num % 10)
    else:
        num = num // 10
        values.append(num % 10)

digits = ''
for i in values:
    digits += str(i)
    digits += ' '

print(digits)

# What does the following code do? It prints '510' because it concatenates strings

print('5' + '10')

# Refactor the code above to print 15

print(int('5') + int('10'))

# Will an error occur if you try to access index >= len? Yes

foo = ['a', 'b', 'c']

# print(foo[3]) # IndexError

# To what value does the following expression evaluate?

print('foo' == 'Foo') # False

# What will the following code do? Why?

# int('3.1415') # ValueError, not an int

# To what value does the exp eval?

print('12' < '9') # True