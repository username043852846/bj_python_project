# import random

# a = random. randrange(1, 10)

# 리스트에 랜덤하게 100개 넣고 그 다음에 가장 큰 수 가장 작은 수 뽑기

# 문자열을 input으로 받아서 거꾸로 출력


# 랜덤한 값 100개 출력
import random
a = []
for i in range(100):
    b = random.randrange(1, 100)
    a.append(b)
print(a)
c = a[0]
d = a[0]
for i in range(100):
    if c < a[i]:
        c = a[i]
    if d > a[i]:
        d = a[i]
print(c)
print(d)



i = (input())

for n in range(len(i)):
    print(i[n])
for n in range(len(i)):
    print(i[len(i)-n-1])




