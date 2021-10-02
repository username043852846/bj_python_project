# 다리 건너기
# 8번의 찬스
# 17개
'''
1. 다리 생성해하는거.
2. 진행하는거 코드 짜기
3. 코드 완료되면 -> 함수화를 어디를 시킬지 결정하고 시킴.
'''

# import random
#
#
# a = []
# b = []
# for i in range(17):
#     comter_enter = random.randrange(0, 2)
#     if comter_enter == 0:
#         comter_enter = '■'
#         comter_enter_2 = '□'
#     elif comter_enter == 1:
#         comter_enter = '□'
#         comter_enter_2 = '■'
#     a.append (comter_enter)
#     b.append (comter_enter_2)
#
# print (a)
# print (b)


#가장 좋은 코드
# bridge = []
# life = 8
#
# for i in range(8):
#     a = random.randrange(0,2)
#     bridge.append(a)
# count = 0
# while life != 0 and count != 7:
#
#     ch = int(input('enter your choice 방탄 or dead : (0.1)'))
#
#     if bridge[count] == ch:
#         count += 1
#         print('살음')
#     else:
#         print('you died')
#         life = life - 1
#
#     if count == 7:
#         print('kkkkkk')


# 틱택토
tic_map = [''for i in range(9)]
tic_map: [0, 0, 0, 0, 0, 0, 0, 0, 0]

[0][1][2]
[3][4][5]
[6][7][8]

tic_map = []
for i in range(9):
    tic_map.append(0)
    