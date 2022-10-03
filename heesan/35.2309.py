# 일곱 난쟁이

# 9명 중에 7명을 찾아야 함
# hint : 일곱 난쟁이의 키의 합이 100이 됨.

# 아홉 난쟁이의 키가 주어졌을 때, 백성공주를 도와 일곱 난쟁이를
# 찾는 프로그램을 작성하시오.

# 입력: 키는 100을 넘지 않는 자연수 , 키는 모두 다르다.
# 여러가지인 경우 아무거나 출력한다.

# 출력: 키를 오름차순으로 정렬한다. 일곱 난쟁이를 찾을 수 없는 경우는 없다.
import sys
import random
small = []
for i in range(9):
    small.append(int(sys.stdin.readline()))

while True: # 합이 100될때까지 7개 무작위
    picked_small = random.sample(small, 7)
    sum_small = sum(picked_small)
    if sum_small == 100:
        break

picked_small.sort()  ## 오름차순 정렬


for i in range(7):
    print(picked_small[i])
