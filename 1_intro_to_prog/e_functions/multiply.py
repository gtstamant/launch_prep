def multiply(num1, num2):
    return num1 * num2

def get_number(prompt):
    entry = input(prompt)
    return float(entry)

num1 = get_number('Enter the first number: ')
num2 = get_number('Enter the second number: ')

product = multiply(num1, num2)

print(f'{num1} * {num2} = {product}')

# Consider the following code and identify the parts

# function name       # multiply_numbers
# function arguments  # 2, 3, 4
# function definition # def … result
# function body       # result = … result
# function parameters # num1, num2, num3
# function invocation # multiply_numbers(2, 3, 4)
# function return val # 24
# all identifiers     # multiply_numbers, num1, num2, num3, result, product

# Identify all identifiers:

# multiply, left, right
# get_num, prompt
# float, input
# first_number
# second_number
# product
# print

# Classify identifiers as global, local, or built-in

# multiply      # global
# left          # local
# right         # local
# get_num       # global
# prompt        # local
# float         # built-in
# input         # built-in
# first_number  # global
# second_number # global
# product       # global
# print         # built-in

# Identify all function names and parameters

# Function names: multiply (1, 9), get_num (4, 7, 8), float, (5)
#     input (5), print(10)
# Parameters: left, right (1); prompt (4)