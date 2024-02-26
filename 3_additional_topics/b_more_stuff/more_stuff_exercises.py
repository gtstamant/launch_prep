### Question 1 ###

# def do_something(dictionary):
#     return sorted(dictionary.keys())[1].upper()

# my_dict = {
#     'Karl':     108,
#     'Clare':    175,
#     'Karis':    140,
#     'Trevor':   180,
#     'Antonina': 132,
#     'Chris':    101,
# }

# It returns CHRIS; technically, the print function is outside the function

### Question 2 ###

# import math

# print(math.sqrt(37))

# def find_sqrt(num):
#     print(math.sqrt(num))

# find_sqrt(37)

# def approx_sqrt(num):
#     epsilon = 0.00001
    
#     max_val = num
#     min_val = 0
#     guess = ((max_val - min_val) / 2) + min_val

#     while abs(num - (guess ** 2)) > epsilon:
#         if guess ** 2 > num:
#             max_val = guess
#             guess = ((max_val - min_val) / 2) + min_val
#         else:
#             min_val = guess
#             guess = ((max_val - min_val) / 2) + min_val
    
#     return guess

# print(approx_sqrt(37))

### Question 3 ###

# def print_sum_of_squares(num1, num2):
#     def sum_of_squares(num1, num2):
#         def square(number):
#             return number * number
#         return (square(num1) + square(num2))
#     print(sum_of_squares(num1, num2))

# print_sum_of_squares(3, 4)
# print_sum_of_squares(5, 12)

### Question 4 ###

# counter = 0

# def increment_counter():
#     global counter
#     counter += 1

# print(counter)                # 0

# increment_counter()
# print(counter)                # 1

# increment_counter()
# print(counter)                # 2

# counter = 100
# increment_counter()
# print(counter)                # 101

### Question 5 ### 

def all_actions():
    counter = 0

    def increment_counter():
        nonlocal counter
        counter += 1

    print(counter)                # 0

    increment_counter()
    print(counter)                # 1

    increment_counter()
    print(counter)                # 2

    counter = 100
    increment_counter()
    print(counter)                # 101

all_actions()