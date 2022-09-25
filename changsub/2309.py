# 2초 => 2억번 연산 가능 => 여유로운 편
heights = []
sum = 0
target = 100
for _ in range(9):
    height = int(input())
    heights.append(height)
    sum += height

differ = sum - target

not_dwarf = []

for i in range(len(heights)):
    find_target = differ - heights[i]
    if find_target in heights and find_target != heights[i]:
        not_dwarf.append(heights[i])
        not_dwarf.append(find_target)
        break

for elem in not_dwarf:
    heights.remove(elem)

heights.sort()
for elem in heights:
    print(elem)
