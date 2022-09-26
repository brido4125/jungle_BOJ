# 연산자 끼워 넣기

N = int(input())

num_list = list(map(int, input().split()))

op_list = list(map(int, input().split()))

copy_op = op_list

answer_list = []


def backTracking(res, L):
    if L == N - 1:
        # tree 끝까지 선정 됨
        answer_list.append(res)
    else:
        # 뽑았던 연산자는 안 뽑는 걸로 => count를 -1
        for i in range(4):
            if i == 0 and op_list[i] > 0:  # 덧셈 가능
                if L == 0:
                    target = num_list[L] + num_list[L + 1]
                else:
                    target = res + num_list[L + 1]
                priv = res
                res = target
                op_list[i] -= 1
                backTracking(res, L + 1)
                op_list[i] += 1
                res = priv
            elif i == 1 and op_list[i] > 0:
                if L == 0:
                    target = num_list[L] - num_list[L + 1]
                else:
                    target = res - num_list[L + 1]
                priv = res
                res = target
                op_list[i] -= 1
                backTracking(res, L + 1)
                op_list[i] += 1
                res = priv
            elif i == 2 and op_list[i] > 0:
                if L == 0:
                    target = num_list[L] * num_list[L + 1]
                else:
                    target = res * num_list[L + 1]
                priv = res
                res = target
                op_list[i] -= 1
                backTracking(res, L + 1)
                op_list[i] += 1
                res= priv
            elif i == 3 and op_list[i] > 0:
                if L == 0:
                    if num_list[L] < 0 and num_list[L + 1] > 0:  # 음수를 양수로 나누는 경우
                        target = -(-num_list[L] // num_list[L + 1])
                    else:
                        target = num_list[L] // num_list[L + 1]
                else:
                    if res < 0 and num_list[L + 1] > 0:  # 음수를 양수로 나누는 경우
                        target = -(-res // num_list[L + 1])
                    else:
                        target = res // num_list[L + 1]
                priv = res
                res = target
                op_list[i] -= 1
                backTracking(res, L + 1)
                op_list[i] += 1
                res = priv


backTracking(0, 0)
print(max(answer_list))
print(min(answer_list))
