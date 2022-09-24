# 입력
# 첫째 줄에 첫 번째 장대에 쌓인 원판의 개수 N (1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄에 옮긴 횟수 K를 출력한다.

# N이 20 이하인 입력에 대해서는 두 번째 줄부터 수행 과정을 출력한다. 두 번째 줄부터 K개의 줄에 걸쳐 두 정수 A B를 빈칸을 사이에 두고 출력하는데, 이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻이다. N이 20보다 큰 경우에는 과정은 출력할 필요가 없다.

# 예제 입력 1
# 3
# 예제 출력 1
# 7
# 1 3
# 1 2
# 3 2
# 1 3
# 2 1
# 2 3
# 1 3

given_number = int(input())


def hanoi(n, a, c, b):
    if n == 1:
        print(a ,c)
    else:
        hanoi(n-1, a, b, c)
        hanoi(1, a, c, b)
        hanoi(n-1, b, c, a)

print(2**given_number - 1)
if given_number <= 20:
    hanoi(given_number, 1, 3, 2)
