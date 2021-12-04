# id = []
# pwd = []
# for i in range(5):
#     a = input()
#     id.append(a)
#
# for i in range(5):
#     b = input()
#     pwd.append(b)
#
# print(id, pwd)


id_list = []
pwd_list = []
for i in range(5):
    temp_id = input("enter the your id :")
    for i in range(len(id_list)):
        if id_list[i] == temp_id:
            print('입력된 id가 중복되었습니다 다시 입력해주세요')
            i = i-1
            continue
    id_list.append(temp_id)
    temp_pwd = input("enter the your pwd :")
    pwd_list.append(temp_pwd)

print(id_list, pwd_list)