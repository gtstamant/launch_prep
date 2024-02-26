import copy

orig = [[1, 2], 3, 4]
dup = copy.copy(orig)

# print(orig is dup)           # False
# print(orig == dup)           # True
orig[2] = 44
# print(dup)                   # [[1, 2], 3, 4]

print(orig[2] is dup[2])
print(orig[0] is dup[0])     # True
# orig[0][1] = 22
# print(dup[0])                # [1, 22]