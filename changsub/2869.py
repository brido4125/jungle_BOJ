A, B, V = map(int, input().split())

# 설명 완벽히 하기
target = V - A
afford = A - B
days = (target // afford) + 1
if target % afford != 0:
    days += 1

print(days)


