a = int(input())

list1 = list(map(int, input().split()))
# print(list1)
count = 0
# list1 = map(int, input().spilt())

# print(a)
# print(list1)

# 리스트의 각 요소들에 대해서 1보다 큰 자기보다 작은수로

# for i in list1: # [1,3,5,7] 을 순회하면서
#     for j in range(len(list1)):
#         if j != 0 or j != 1:
#             if i % j == 0:
#                 count = count + 1

for i in list1:
    error = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                error += 1
        if error == 0:
            count += 1


print(count)
