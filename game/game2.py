# function , 함수
# 다리 건너기
# 8번의 찬스
# 17개
'''
1. 다리 생성해하는거.
2. 진행하는거 코드 짜기
3. 코드 완료되면 -> 함수화를 어디를 시킬지 결정하고 시킴.
'''

# def login(x, y):
#     z = x + y
#     # 함수를 종료
#     # 값을 반환한다.
#     return z
#
# result = login(3, 2)
# import random
#
# print(result)

# 1. 랜덤하게 10개를 집어넣는거를 함수화 시키고 리턴으로 리스트를 받아
#        make_random_list
# 2. 리턴 받은 리스트를 입력으로 놓고 여기서 최고 값만 리턴 받아서 출력
#        find_max_value
#
# import random
# def make_random_list():
#     a = []
#     for i in range(10):
#         random_num = random.randrange(1, 10)
#         a. append(random_num)
#     return a
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
# def find_max_value(a):
#     max_value = a[0]
#     for i in range(len(a)):
#         if max_value < a[i]:
#             max_value = a[i]
#     return max_value
# print(find_max_value(make_random_list()))



# 간단한 게임
    # coin 600원이 주어짐.
    # 가위 바위 보 s, r, p
    # 컴퓨터도 600원이 있고 s, r, p 를 선택
    # 한판당 200원 빵
    # 그래서 플레이가 돈이 바닥 날떄 까지 게임 진행.
import random
user_coin = 600
com_coin = 600

user_enter = input('enter r, s, p :')

comter_enter = random.randrange(0, 3)
if comter_enter == 0:
    comter_enter = 'r'
elif comter_enter == 1:
    comter_enter = 's'
elif comter_enter == 2:
    comter_enter = 'p'

# 비김
if user_enter == comter_enter:
    print('draw')
#승리
elif user_enter == 'p' and comter_enter =='r':
    print('win')
elif user_enter == 's' and comter_enter == 'p':
    print('win')
elif user_enter == 'r' and comter_enter == 's':
    print('win')

#패배
elif user_enter == 'r' and comter_enter =='p':
    print('lose')
elif user_enter == 'p' and comter_enter == 's':
    print('lose')
elif user_enter == 's' and comter_enter == 'r':
    print('lose')
user_coin(i-100)

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
