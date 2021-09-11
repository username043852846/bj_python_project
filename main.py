









# server, client

#id 중복제거
#id 8
#pwd !,@,#


# id_list = []
# pwd_list = []

# for i in range(5):
#     temp_id = input('enter your id')
#     for i in range(len(id_list)):

# print('{} x {} = {}'.format(1, 2, 3))

# for i in range(1, 10):
#     for j in range(1, 10):
#         print('{} x {} = {}'.format(i, j, i*j))

import random
a = []
for i in range(100):
    b = random.randrange(1, 6)
    a.append(b)

count_list = [0,0,0,0,0]
for i in range(len(a)):
    num = a[i] -1
    count_list[num] +=1
print(count_list)














