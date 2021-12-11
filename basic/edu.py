# 1
# 3, 2, 1, 23
#
# 2, 3, 1, 23
#
# 2, 1, 3, 23
#
# 2, 1, 3, 23

# 2
# 1, 2, 3, 23

# 3

# 4

# 1, 2, 3, 23

# random number 5

# Bubble sorting


import random

# a = []
# for i in range(5):
#     a.append(random.randrange(100))
# print(a)
#     for i in range(4):
#         if a[i] > a[i+1]:
#             a[i], a[i+1] = a[i+1], a[i]


# a = []
# for i in range(5):
#     a.append(random.randrange(100))
# for i in range(10):
#     if a[i] > a[i+1]:
#         a[i+1], a[i] = a[i], a[i+1]
#
#     print(a)

# selective sort

# 3, 5, 1, 2

# 1, 5, 3, 2

# 1, 2, 3, 5

# 1, 2, 3, 5

a = []
for i in range(5):
    a.append(random.randrange(1, 100))
print(a)
for i in range(5):
    if min < a[i]:
        min = a[i]
    elif max > a[i+3]:
        max = a[i+3]
