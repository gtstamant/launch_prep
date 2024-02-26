### Problem 2 ###

# age = int(input('How old are you? '))

# print(f'You are {age} years old. \n')

# for year in range(10, 50, 10):
#     print(f'In {year} years, ' 
#           f'you will be {age + year} years old.')

### Problem 3 ###

# my_list = [6, 3, 0, 11, 20, 4, 17]

# index = 0
# while index < len(my_list):
#     print(my_list[index])
#     index += 1

# print('\n Switching to for loop. \n')

# for num  in my_list:
#     print(num)

### Problem 4 ###

# my_list = [6, 3, 0, 11, 20, 4, 17]

# index = 0
# while index < len(my_list):
#     if my_list[index] % 2 == 0:
#         print(my_list[index])
#     index += 1

# print()

# for num in my_list:
#     if num % 2 != 0:
#         print(num)

### Problem 5 ###

# my_list = [
#     [1, 3, 6, 11],
#     [4, 2, 4],
#     [9, 17, 16, 0],
# ]

# for list in my_list:
#     for item in list:
#         if item % 2 == 0:
#             print(item)

### Problem 6 ###

# my_list = [
#     1, 3, 6, 11,
#     4, 2, 4, 9,
#     17, 16, 0,
# ]

# # new_list = ['even' if num % 2 == 0 else 'odd'
# #             for num in my_list ]

# # print(new_list)

# def odd_or_even(number):
#     return 'even' if number % 2 == 0 else 'odd'

# new_list = [odd_or_even(num) for num in my_list]

# print(new_list)

### Problem 7 ###

# my_tuple = (1, 'a', '1', 3, [7], 3.1415,
#             -4, None, {1, 2, 3}, False)

# # def find_integers(tup):
# #     int_list = []
# #     for item in tup:
# #         if type(item) is int:
# #             int_list.append(item)
# #     return int_list

# def find_integers(tup):
#     int_list = [item for item in tup 
#                 if type(item) is int]
#     return int_list

# integers = find_integers(my_tuple)
# print(integers)                    # [1, 3, -4]

### Probelm 8 ###

# my_set = {
#     'Fluffy',
#     'Butterscotch',
#     'Pudding',
#     'Cheddar',
#     'Cocoa',
# }

# new_dict = {item: len(item) for item in my_set
#             if len(item) % 2 != 0}
# print(new_dict)

### Problem 9 ###

# def factorial(n):
#     total = 1
#     for item in range(2, n + 1):
#         total *= item
#     return total

# print(factorial(25))

# def rec_factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * rec_factorial(n - 1)

# print(rec_factorial(5))

### Problem 10 ###

# import random

# highest = 10

# while True:
#     number = random.randrange(highest + 1)
#     print(number)
#     if number == highest:
#         break

### Problem 11 ###
    
my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

index = 0
while index < len(my_list):
    nested_index = 0
    while nested_index < len(my_list[index]):
        item = my_list[index][nested_index]
        if is_even(item):
            print(item)
        nested_index += 1
    index += 1
