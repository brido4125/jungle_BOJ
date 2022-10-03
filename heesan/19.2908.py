a, b = list(map(int, input().split()))
list1 = []
# a 가 123 이면
changeA = (a//100) + (((a % 100)//10) * 10) + ((a % 10) * 100)
changeB = (b//100) + (((b % 100)//10) * 10) + ((b % 10) * 100)
list1.append(changeA)
list1.append(changeB)

print(list1)

# for문 인덱스를 역순으로 reverse 배열에 담는다.
if list1[0] > list1[1]:
    print(list1[0])
else:
    print(list1[1])


# revese 요소들을 하나의 문자열로 합친다 (합치는 과정에서 더이상 리스트형이 아님)
# 정수로 형변환 한다.
# 크기 비교해서 큰 쪽을 출력한다.
