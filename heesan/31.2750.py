# 수 정렬하기 1 (삽입정렬)
import sys
N = int(sys.stdin.readline())
array = [sys.stdin.readline().strip() for i in range(N)]

for i in range(1, len(array)):
    temp_value = array[i]
    position = i - 1

    while position >= 0:
        if array[position] > temp_value:
            array[position + 1] = array[position]
            position = position - 1
        else:
            break

    array[position + 1] = temp_value

for i in array:
    print(i)
