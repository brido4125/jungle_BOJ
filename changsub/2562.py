max = 0
count = 0
index = 0
# 배열에 할당해서 max() 메서드 쓰지 않고 풀기
for _ in range(9):
    target = int(input())
    count += 1
    if max < target:
        max = target
        index = count
print(max)
print(index)

