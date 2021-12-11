# money

# 300

# greedy 적용해서 가장 적게 줄 수 있는 동전의 수
# 500, 100, 50, 10

# 3, (100, 100, 100) or (100 * 3)

# 경우의 수 중 최선의 선택 = 목표까지 도달하기 가장 빠른 경우의 수

# if문으로만 하는 방법
# a = int(input('지불할 금액:'))
#
# # 500원
# if a > 500:
#     b = a // 500
#     c = a % 500
# elif a < 500:
#     c = a
# # 100원
# elif c > 100:
#     d = c // 100
#     e = c % 100
# elif a < 500 or c < 100:
#     e = a or e = c
# # 50원
# elif e > 50:
#     f = e // 50
#     g = e % 50
# # 10원
# elif g > 10:
#     h = g // 10
#     i = g % 10
#
# money[500, 100 , 50 , 10]





# for문으로 하는 방법

# for i in range(len(changes)):
#     change = changes[i]
#
#     count += money // change
#
#     count += money // change

import random
random.randrange(0, 100)
for i in rnage(