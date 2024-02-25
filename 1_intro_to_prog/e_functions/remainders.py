def remainders_5(numbers):
    return [number % 5 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # False
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]            # True
numbers_3 = [0, 5, 10]                          # False
numbers_4 = []                                  # True

def print_output(list):
    for element in list:
        print(all(remainders_5(element)))

print_output([numbers_1, numbers_2, numbers_3, numbers_4])