import math
from collections import Counter
from itertools import combinations_with_replacement
from itertools import count, product
from itertools import combinations
from itertools import permutations
import sys
from this import d

from pkg_resources import ResolutionError
# 지수 표현은 실수형 데이터로서 처리됨 , 임의의 큰 수를 표현하기 위해 사용

# int() 정수형 데이터로 바꿔주는 내장함수임.

# a = 1e9
# print(a)

# a = int(1e9)
# print(a)

# a = 0.3 + 0.6
# print(a)

# if (a == 0.9):
#     print(True)
# else:
#     print(False)
# 이럴 때 round()함수 이용 반올림목적임.

# ex)
# print(round(123.456,2))
# 반올림해서 소수 둘째자리 까지 나타내라.

# 파이썬에서 나누기 연산자(/)는 실수형으로 반환함
# 파이썬에서는 몫 연산자(//)를 사용함
# 거듭제곱 연산자 **

# 리스트 자료형 혹은 테이블이라고도 부름 -> 데이터를 연속적으로 담아 처리하기 위해 사용하는 자료형
# 리스트는 []안에 원소를 넣어 초기화 , 쉼표(,)로 원소 구분
# 비어있는 리스트 선언할때는 list() 혹은 간단히 lis = [] 라고 해도 됨.

# 크기가 N이고 , 모든 값이 0 인 1차원 리스트 초기화
# n = 10
# a = [0] * n
# print(a)

# 리스트의 특정한 원소에 접근하는 것을 인덱싱이라고 한다.
# 음의 정수를 넣으면 원소를 거꾸로 탐색하게 됨. 주의! -1부터임.
# 리스트에서 연속적인 위치를 갖는 원소들을 가져와야 할 때는 슬라이싱 이용한다.
# 대괄호 안에 콜론(:)을 넣어서 시작 인덱스와 끝 인덱스를 설정할 수  있ㅏ.
# 끝 인덱스는 실제 인덱스보다 1을 더 크게 설정한다.
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# print(a[1:4]) # 2 3 4

# -------------------------------------------------------------------------------------

# 리스트 컴프리헨션
# 리스트 컴프리헨션은 2차원 리스트를 초기화할 때 효과적으로 사용될 수 있다.
# 대괄호 안에 조건문과 반복문을 적용하여 리스트를 초기화 할 수 있다.
# array = [i for i in range(10)]  # 반복문부터 작성하는 걸 추천함
# print(array) # 단 한줄만에 리스트를 초기화 할 수 있다.

# array = [i for i in range(20) if i % 2 == 1]
# print(array)

# 반복문을 사용한다면!!.....

# array = []
# for i in range(20):
#     if i % 2 == 1:
#         array.append(i)

# print(array)


# array = [i * i for i in range(1, 10)]
# print(array)

# array = [0] * 3
# print(array)
# array = [[0] * 3 for _ in range(3)]  # 2차원 배열
# print(array)

# n = 4
# m = 3
# array = [[0] * m * n]
# print(array)

# array = [1,2]
# array.reverse() # 요소의 순서를 뒤집는다.
# print(array)

# a = [4, 3, 2, 1]

# a.reverse()
# print(a)  # [1,2,3,4]

# a.insert(2, 3)
# print(a)  # [1,2,3,3,4]

# print("값이 3인 데이터 개수:", a.count(3))  # 2

# a.remove(1)
# print(a)  # [2,3,3,4]

# a = [1, 2, 3, 4, 5, 5, 5]
# remove_set = {3, 5}

# result = [i for i in a if i not in remove_set] # 제거 대상이 아닌 경우에만 남겨 놓는다.

# -------------------------------------------------------------------------------------

# 문자열 자료형
# data = 'Hello World'
# print(data)

# data = "나는 \"김희산\"이다"
# print(data)

# a = "Hello"
# b = "World"
# print(a + " " + b)

# a = "String"
# print(a * 3)

# a = "ABCEDF"
# print(a[2: 4])

# -------------------------------------------------------------------------------------

# 튜플 자료형은 리스트와 유사 but 문법적 차이가 있다
# 한번 선언된 값을 변경 할 수 없다!
# 소괄호를 사용한다.
# 리스트에 비해 상대적으로 공간 효율적이다.

# a = (1, 2, 3, 4, 5, 6, 7, 8)
# print(a[3])
# print(a[1: 5])


# 리스트와는 다르게 a[2] = 7 (오류❌)한번 선언된 값 변경 불가!
# 튜플을 사용하면 좋은 경우
# 1.서로 다른 성질의 데이터를 묶어서 관리할 때
#   >> 최단 경로 알고리즘에서는 ( 비용, 노드 번호)의 형태로 튜플 자료형을 자주 사용함
# 2.데이터의 나열을 해싱(Hashing)의 키 값으로 사용해야 할 때
#   >> 튜플은 변경이 불가능하므로 리스트와 다르게 키 값으로 사용될 수 있다.
# 3.리스트보다 메모리를 효율적으로 사용해야 할 때

# -------------------------------------------------------------------------------------
# 사전 자료형은 키와 값의 쌍을 데이터로 가지는 자료형이다.
# 파이썬의 사전 자료형은 해시 테이블을 이용하므로 데이터의 조회 및 수정에 있어서
# O(1)의 시간에 처리 할 수 있다.

# data = {"사과": 'apple'}
# print(data)


# lis = dict()
# lis['사과'] = 'apple'
# lis['바나나'] = 'banana'
# lis['메론'] = 'melon'
# print(lis)

# if '사과' in data:
#     print("'사과'를 키로 가지는 데이터가 존재합니다.")

# key_list = lis.keys()  # list() 사용하면 list 형태 형변환이 가능하다.(보통 이렇게 형변환해서 사용한다)
# value_list = lis.values()

# print(key_list)
# print(list(key_list))

# print(value_list)
# print(list(value_list))

# for key in key_list:
#     print(lis[key])

# print(lis['사과'])

# -------------------------------------------------------------------------------------
# 집합 자료형
# 중복을 허용하지 않는다
# 순서가 없다
# 데이터가 존재하는지 존재안하는지 그 여부만 체크할때 효과적이다.
# 집합은 리스트 혹은 문자열을 이용해서 초기화 할 수 있다. set() 함수 이용
# 혹은 중괄호 ({}) 안에 각 원소를 콤마(,) 기준으로 구분하여 삽입함으로써 초기화 할 수 있다.
# 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있다.

# # 집합 자료형 초기화 방법 1
# data = set([1, 1, 2, 3, 4, 4, 5])  # 중복 요소 삭제
# print(data)

# # 집합 자료형 초기화 방법2
# data = {1, 1, 2, 3, 4, 4, 5}  # 중복 요소 한번만 출력
# print(data)

# # 집합 자료형 연산
# a = set([1, 2, 3, 4, 5])
# b = set([3, 4, 5, 6, 7])

# print(a | b)  # {1,2,3,4,5,6,7}
# print(a & b)  # {3,4,5}
# print(a - b)  # {1,2}

# data = set([1, 2, 3])
# print(data)

# data.add(4)
# print(data)

# data.update([5, 6])
# print(data)

# data.remove(3)
# print(data)

# ⭐️ 사전 자료형과 집합 자료형의 특징 ⭐️
# - 리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있음
# - 사전자료형과 집합 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없음
#   - 사전의 키(Key)혹은 집합의 원소를 이용해 O(1)의 시간 복잡도로 조회한다.
# ❗️이 때, 키나 원소의 값으로는 변경 불가능한 문자열이나 튜플과 같은 객체가 사용되어야 한다.


# -------------------------------------------------------------------------------------

# 기본 입출력
# a = int(input())

# # a,b,c를 공백을 기준으로 구분하여 입력
# # a, b, c = map(input().split()) # 데이터의 개수가 많지 않을 때.


# lis = list(map(int, input().split()))
# lis.sort(reverse=True)

# print(lis)

# lis.sort()
# print(lis)


# print()는 기본적으로 출력 이후에 줄 바꿈을 수행한다
# 줄 바꿈을 원치 않는 경우 'end' 속성을 이용할 수 있다.


# 뭘 입력하든지간에 문자열로 받음

# data = sys.stdin.readline().rstrip()
# print(data)


# a = 1
# b = 2
# print(a, b)
# print(a, end=" ")  # 줄바꿈이 생기지 않는다.
# print(b, end=" ")  # 그 다음 출력값이 왔을 때 줄바꿈이 생기지 않는다.

# answer = 7
# f = 10
# # f-string {}안에 변수명 적기 자바스크립트에서 백틱이랑 같은 효과.
# print(f"정답은  {str(answer)} {f}  입니다.")


# 파이썬의 기타 연산자
# 다수의 데이터를 담는 자료형을 위해 in연산자와 not in 연산자가 제공된다
# 리스트,튜플,문자열,딕셔너리 모두에서 사용이 가능하다.

# a = 30

# if a >= 50:
#     pass  # 일단 비워두고 실행하고 싶을 때.
# else:
#     result= "a < 50"
# print(result)


# 조건문의 간소화
# 조건문에서 실행될 소스코드가 한 줄인 경우, 굳이 줄 바꿈을 하지 않고도 간략하게 표현할 수 있다

# score = 85

# if score >= 80: result = "Success"
# else: result = "Fail"
# print(result)

# 조건부 표현식(Conditional Expression)은 if~else 문을 한 줄에 작성할 수 있도록 해준다.
# score = 85
# result = "Success" if score >= 80 else "Fail"
# print(result)


# x = 15
# if 0 < x < 20: # 파이썬에선 수학의 부등식을 그대로 사용할 수 있다.
#     result = "true"
# print(result)


# continue 키워드
# 반복문에서 남은 코드의 실행을 건너뛰고, 다음 반복을 진행하고자 할 때 continue를 사용한다
# 1부터 9까지의 홀수의 합을 구할 때 다음과 같이 작성할 수 있습니다.

# result = 0

# for i in range(1, 10):
#     if i % 2 == 0:
#         continue
#     result = result + i

# print(result)


# break 키워드
# 반복문을 즉시 탈출하고자 할 때 break를 사용한다
# 1부터 5까지의 정수를 차례대로 출력하고자 할 때 다음과 같이 작성할 수 있다.

# i = 1

# while True:
#     print("현재 i의 값", i)
#     if i == 5:
#         break # 즉시 탈출!
#     i = i + 1


# scores = [90, 85, 77, 65, 97]

# for i in range(5):
#     if scores[i] >= 80:
#         print(i+1, "번 학생은 합격입니다")


# cheating_student_list = {2, 4}  # 2번 학생, 4번 학생 실질적인 index는 [1]번 학생 [3]번 학생이다

# 의마하는 바는 index[0] 부터 index[4] 까지의 해당하는 원소가 차례대로 들어오겠다는 의미임.
# for i in range(5):
#     if i+1 in cheating_student_list:
#         continue  # 남은 코드의 실행을 건너뛰고 다음반복을 실행한다.
#     if scores[i] >= 80:
#         print(i+1, "번 학생은 합격입니다")


# def add(a, b):
#     return a + b


# def subtract(a, b):
#     return a - b


# result = add(3, 7)
# print(result)

# # 파라미터의 변수를 직접 지정 할 수 있음
# result = add(b=5, a=7)
# print(result)

# global 키워드로 변수를 지정하면 해당 함수에는 지역 변수를 만들지 않고
# 함수 바깥에 선언된 변수를 바로 참조하게 된다.
# a = 0


# def func():
#     global a
#     a += 1
# # 아니면 다시 할당해줘야 함 함수안에서


# def func():
#     a = 0
#     a += 1


# for i in range(10):
#     func()
# print(a)

# a = 10


# # 단순히 전역변수로 선언되어 있는 값을 그대로 출력하는 등 그대로 값을 참조하는 경우에는 오류 없이 수행됨.
# def func():
#     print(a)


# func()

# array = [1, 2, 3, 4, 5]


# def func():
#     array.append(6)
#     print(array)


# func()

# array = [1, 2, 3, 4, 5]


# def func():
#     array = [7, 8, 9]
#     array.append(10)
#     print(array)


# func()  # [7, 8, 9, 10]
# print(array)  # [1, 2, 3, 4, 5]
# ❗️전역변수 지역변수 차이점 숙지. 문제풀 때 실수 없이 풀 수 있어야 함.

# 람다 표현식 : 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다는 점이 특징입니다

# 일반적인 함수표현식


# def add(a, b):
#     return a + b


# print(add(3, 7))

# # 람다 표현식으로 구현한 add() 메서드
# print((lambda a, b: a + b)(50, 25))
# # 예시

# array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]


# def my_key(x):
#     return x[1]


# print(sorted(array, key=my_key))
# print(sorted(array, key=lambda x: x[1]))

# # 람다표현식 예시: 여러 개의 리스트에 적용
# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]

# # map 함수는 각각의 원소에 어떠한 함수를 적용하고자 할 때 사용
# result = map(lambda a, b: a+b, list1, list2)
# print(list(result))


# # 순열 : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
# # -- {"A","B","C"} 에서 두 개를 선택하여 나열하는 경우 : 'ABC','ACB','BAC','BCA','CAB','CBA'
# data = ['A', 'B', 'C']  # 데이터 준비
# result = list(permutations(data, 3))  # 모든 순열 구하기
# print(result)


# # 조합 : 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것
# # -- {"A","B","C"} 에서 순서를 고려하지 않고 두 개를 뽑는 경우 : 'AB','AC','BC'\

# data = ['A', 'B', 'C']  # 데이터 준비
# result = list(combinations(data, 2))
# print(result)

# # 중복 순열과 중복 조합

# data = ['A', 'B', 'C']  # 데이터 준비
# result = list(product(data, repeat=2))
# print(result)

# data = ['A', 'B', 'C']  # 데이터 준비
# result = list(combinations_with_replacement(data, 2))
# print(result)

# # Counter
# # 파이썬 collections 라이브러리의 Counter 는 등장 횟수를 세는 기능을 제공한다.
# # 리스트와 같은 반복 가능한(iterable) 객체가 주어졌을 때 내부의 원소가 몇 번 등장했는지를 알려준다


# counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

# print(counter['blue'])  # 3 'blue'가 등장한 횟수 출력
# print(counter['red'])  # 2 'red'가 등장한 횟수 출력
# print(counter['green'])  # 1 'green'가 등장한 횟수 출력

# print(dict(counter))  # 사전 자료형으로 반환


# # 최대 공약수와 최소 공배수
# # math 라이브러리의 gcd() 함수를 이용 할 수 있다.


# # 최소 공배수를 (LCM)를 구하는 함수
# def lcm(a, b):
#     return a*b // math.gcd(a, b)


# print(math.gcd(21, 14))  # 최대 공약수(GCD) 계산
# print(lcm(21, 14))  # 최소 공배수(LCM) 계산


# 인덱싱과 슬라이싱을 이용한 리스트 수정시 주의사항
# my_list = [1, 2, 3, 4, 5]
# my_list[2] = ['a', 'b', 'c'] # 리스트의 두 번째 요소를 ['a', 'b', 'c']로 교체
# [1, 2, ['a', 'b', 'c'], 4, 5] # 리스트가 하나의 요소로 들어가버린다.

# my_list = [1, 2, 3, 4, 5]
# my_list[2:3] = ['a', 'b', 'c'] # 리스트의 두 번째 요소부터 세 번째 요소 사이의 리스트를 ['a', 'b', 'c']로 교체
# my_list
# [1, 2, 'a', 'b', 'c', 4, 5]

# 삭제 >> []을 사용하여 요소 삭제
# my_list = [1, 2, 3]
# my_list[1:3] = [] # 인덱스 1번부터 2번까지 삭제함
# print(my_list) #[1]


# del 함수를 이용한 리스트에서의 요소 삭제
# my_list = [1, 2, 3]
# del my_list[1]
# print(my_list)  # [1,3]

# my_list2 = [10, 20, 30, 40, 50]
# del my_list2[2: 5]
# print(my_list2) # [10,20]

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

my_list2 = [1, 2, 3]
my_list2.append([4, 5])
print(my_list2)

my_list3 = [1, 2, 3]
my_list3.extend([4, 5])
print(my_list3)

# 리스트이름.insert(삽입할 위치의 인덱스 값, 삽입할 요소)
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 'a')
print(my_list)  # [1, 2, 'a', 3, 4, 5]


# 하나의 요소를 인자로 받아 리스트 내에서 첫 번째로 일치하는 요소를 삭제한다.
# 리스트이름.remove(삭제할 요소)
my_list4 = ['a', 'd', 'c', 'd', 'e']
my_list4.remove('d')
print(my_list4)

# pop 리스트 요소 꺼내기
# 하나의 인덱스 값을 인자를 받아서 리스트 내에서 해당 인덱스 값의 요소를 삭제하고 삭제한 값을 리턴한다.
# 아무 값도 받지 않을 경우 기본값은 -1. 즉, 제일 마지막 요소를 삭제하고 그 값을 리턴한다.

my_list5 = [100, 200, 300, 400]
print(my_list5.pop(2)) #삭제한 값을 반환함 300 값을 return 함
print(my_list5)
