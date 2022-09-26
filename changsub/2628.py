import sys

x,y = map(int, input().split())
num = int(sys.stdin.readline())
garo_point = [0,x]
sero_point = [0,y]
for _ in range(num):
    dis,point = map(int,sys.stdin.readline().split())
    if dis == 0:#세로의 자를 지점
        sero_point.append(point)
    else:# 가로의 자를 지점
        garo_point.append(point)


garo_point.sort()
sero_point.sort()

max_garo = 0
max_sero = 0

for i in range(len(garo_point)-1):
    if max_garo < abs(garo_point[i] - garo_point[i+1]):
        max_garo = abs(garo_point[i] - garo_point[i+1])

for i in range(len(sero_point)-1):
    if max_sero < abs(sero_point[i] - sero_point[i+1]):
        max_sero = abs(sero_point[i] - sero_point[i+1])


print(max_garo * max_sero)