# 문제
# N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

# 입력
# 첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.

# 출력
# 첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.

# 예제 입력 1
# 6
# 20 1 15 8 4 10
# 예제 출력
# 62

import math
from itertools import permutations
import sys

N = int(input())

lis1 = list(map(int, sys.stdin.readline().split()))
# print(lis1)

# 6개를 나열해서 나오는 모든 튜플을 리스트에 담음
# 리스트에 각 인덱스에 해당하는 원소(튜플)에 반복문 사용
# |A[0] - A[1]| + |A[1] - A[2]| +...+ |A[N-2] - A[N-1]| 값을 리스트에 담음
# 그 리스트에서 최댓값을 찾는다.


sum_list = []
sum = 0
for i in list(permutations(lis1, N)):
    #  i = (20 1 15 8 4 10) 하나씩 순회하면서 계산해서 합을 빈 배열에 담아라.
    for j in range(len(i)-1):
        gap_value = abs((i[j] - i[j+1]))
        sum += gap_value
    sum_list.append(sum)
    sum = 0

print(max(sum_list))
