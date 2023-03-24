array = [5, 3, 1, 6, 7, 2]

for i in range(len(array)):
    min_index = i
    # 인덱스 i 이후로 가장 작은 value 찾기
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    # 찾은 가장 작은 value와 현재 i번재 인덱스를 변경 (swap)
    array[i], array[min_index] = array[min_index], array[i],

print(array)
