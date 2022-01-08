# 1. 숫자 (정수 int, 실수 float)

# 과목 점수 구하기 3개의 과목 점수를 입력 받아 평균 점수를 구하세요.

# a = int(input())
# b = int(input())
# c = int(input())
# print((a+b+c) / 3)

# 2. 문자열
# 문자열의 연산
# 덧셈 = 문자열 붙이기
# 뺄셈 = 문자열 반복
# 인덱싱 = a[n], n은 0부터
# 슬라이싱 = a[n:m:o], n = 시작, m = 끝, o = 오프셋
# a = 'life is too short.'
# print(a[0:5])
# print(a[12:17])
# print(a[::-1]) # 문자열 뒤집기
# 포맷팅(format) = 형식 문자열
# print(" 정수 = %d, 실수 %f, 8진수 = %o, 16진수 = %x, 뮨자열 = %S"
#       % (1, 1.0, 8, 16, "hello"))

# 문제. 주민등록번호 881120~1068234에서 연도, 월, 일을 추출하여 생년월일을 나타내세요.

# number = "881120-10688234"
# year = number[:2]   # 연도
# month = number[2:4] # 월
# day = number[4:6]   # 일
# gender = number[7]  # 성별코드
#
# if gender in ['1', '2']:
#     year = '19' + year # 1900년대
# else:
#     year = '20' + year # 2000년대
# if gender in ['1', '3']:
#     gender = '남자'
# else:
#     gender = '여자'
# print('%s년 %s월 %s일 성별:%s' % (year, month, day, gender))

# 3. 리스트
# list(), []
# 덧셈 = 리스트 붙이기 [] + []
# 곱셈 = 리스트의 내용 반복
# 값추가 = append
# 값제거 = delete, pop, remove
# 정렬 = sort, sorted
# 확장 = extend == 리스트 덧셈
# 갯수 세기 = len, count

# a = [1, 2, 3, 4, 5, 5, 5]
# a.insert(2, 'hello')
# print(len(a), a.count(5))

# 4. 튜플(값을 변경할 수 없는 리스트)
# t1 = ()      비어있는 튜플
# t2 = (1)     값이 하나 있는 튜플
# t3 = (1, 2)  값이 두개 이상 있는 튜플
# t4 = 1, 2, 3 값이 두개 이상이면 괄호 생략가능

# 인덱싱, 슬라이싱 가능
# 덧셈, 곱셈 가능

# 5. 딕셔너리(dictinary = 사전)
# key와 valuㄷ로 이루어진 타입
# 값을 조회할때 => d[key]
# 값을 변경할때 => d[key] = value
# 값을 추가할때 => d[new_key] = value
# 값을 삭제할때 => del d [key]
# d = {True: 'v', 3: '삼', (1, 2): '4'}

# 조회
# print(d[True])

# 변경
# d[3] = 'three'

# 추가
# d['new'] = 'new value'

# 삭제
# del d[(1, 2)]
# print(d)

# key 리스트 만들기 => list(d.keys())
# value 리스트 만들기 => list(d.values())
# key,value 쌍 리스트 만들기 => list(d,items())
# 모든 아이템 => d.clear()

# 6. 집합(set)
# set()
# 순서가 없다, 중복이 없다.
# add(합집합), differnce(차집합), interaction(교집합)
# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# s3 = s1.union(s2)
# print(s3)

# 리스트에서 중복을 제거하고 오름치순으로 정렬하세요
# a = [3, 2, 1, 4, 6, 7, 6, 6, 7]
# b = list(set(a))
# b.sort()
# print(b)

# 7. 불(bool, boolean)
#  단 두가의 값만 가진다. Ture or false
# a = 1
# b = 2
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a < b and a != b)
# print(a > b or a != b)
# print(1 in [1 , 2, 3])
# print(1 not in [1 , 2, 3])
# print(not (1 in [1 , 2, 3]))