'''
1. map을 만든다.
2. 말을 놓는거
3. 맵을 보여주는거 (print)
4. 승부 여부
'''

def make_map():

    tic_map = [" " for i in range(9)]

    '''
    
    tic_map = []
    for i in rnage(9):
        tic_map.append(0)
    '''

    return tic_map

tic_map = make_map()

# int(input('enter the number :'))

# [] 안에 O 또는 X 또는 공백이 들어 갈 수 있어야함


# 단순히 이렇게 넣으면 ok?
# 중복 방지
# 컴퓨터 랜던하게 값을 생성해서 대입
import random

for i in range(9):
    print(tic_map)
    while True:
        pos = int(input("Enter your location : "))
        if tic_map[pos] != " ":
            print('다시')
        else:
            tic_map[pos] = "x"
            break
    while True:
        com_pos = int(random.randrange(0,9))
        print(com_pos)
        if tic_map[com_pos] != " ":
            print('rmrj dksla')
        else:
            tic_map[com_pos] = "y"
            break

if  tic_map(0) == tic_map(1) == tic_map(2):
    tic_map(3) == tic_map(4) == tic_map(5)
    tic_map(6) == tic_map(7) == tic_map(8)
    print('win')

else:
    print('you died')




# 말을 놓는 것.
# tic_map = put_abatar(tic_map)

