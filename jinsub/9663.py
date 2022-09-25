# 문제
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N < 15)

# 출력
# 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

# 예제 입력 1
# 8
# 예제 출력 1
# 92


# <시간 초과> 



def find_space(x):
    global count_case

    if x == input_number:
        count_case += 1

    else:
        for i in range(input_number):
            row[x] = i
            if check(x):
                find_space(x+1)


def check(x):
    for i in range(x):
        if row[i] == row[x] or abs(row[i] - row[x]) == abs(i-x):
            return False
    return True

input_number=int(input())
row = [0] * input_number
count_case = 0
find_space(0)
print(count_case)
