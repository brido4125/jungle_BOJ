minAns = float('Inf')
maxAns = float('-Inf')
N = int(input())
numArr = list(map(int, input().split()))
operator = list(map(int, input().split()))

answers = []


def dfs(level, sum):
    global depth, minAns, maxAns, operator, answers
    if level == depth:
        answers.append(sum)
        return
    else:
        for i in range(len(operator)):
            if i == 0 and operator[0] > 0:
                sum += numArr[level + 1]
                operator[0] -= 1
                dfs(level + 1, sum)
                operator[0] += 1
                sum -= numArr[level + 1]
            elif i == 1 and operator[1] > 0:
                sum -= numArr[level + 1]
                operator[1] -= 1
                dfs(level + 1, sum)
                operator[1] += 1
                sum += numArr[level + 1]
            elif i == 2 and operator[2] > 0:
                sum *= numArr[level + 1]
                operator[2] -= 1
                dfs(level + 1, sum)
                operator[2] += 1
                sum //= numArr[level + 1]
            elif i == 3 and operator[3] > 0:
                # 음수 나누기 처리
                if sum < 0:
                    sum = -(-sum // numArr[level + 1])
                    operator[3] -= 1
                    dfs(level + 1, sum)
                    operator[3] += 1
                    sum *= -numArr[level + 1]
                else:
                    sum = sum // numArr[level + 1]
                    operator[3] -= 1
                    dfs(level + 1, sum)
                    operator[3] += 1
                    sum *= numArr[level + 1]




depth = sum(operator)
dfs(0, numArr[0])
print(max(answers))
print(min(answers))
