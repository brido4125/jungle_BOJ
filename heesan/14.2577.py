
# // 2577번 문제 숫자의 개수

# // 세개의 자연수 A,B,C 받아서 A * B * C 결과가 0부터 9까지 각각의 숫자가 몇번씩 쓰였는지 구하는 프로그램
# // A × B × C = 150 × 266 × 427 = 17037300 이 되고, 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

# // 예제입력
# // 150
# // 266
# // 427
# // 예제출력
# // 3
# // 1
# // 0
# // 2
# // 0
# // 0
# // 0
# // 2
# // 0
# // 0


a = int(input())
b = int(input())
c = int(input())

value = a * b * c

value_list = list(map(int, str(value)))
# print(value_list)  # 문자열로 이루어진 리스트


for i in range(10):  # 0부터 9까지 돈다
    count = 0  # count 초기값 0
    for j in value_list:  # 배열안에 요소들을 순환한다.
        if j == int(i):  # 만약 배열을 순회하면서 배열안에 요소들중에 i값이랑 일치하는 게 있다면
            count = count + 1  # count 에 1을 더해라
    print(count)  # count 출력하고 다시 반복문위로 올라가면서 count = 0 으로 초기화


# 리스트를 비교할 때는 요소의 형태가 같아야 한다. 
