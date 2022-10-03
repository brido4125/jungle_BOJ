import math

x, y = map(int, input().split())
x_list = [0, x]  
y_list = [0, y]  
for _ in range(int(input())):
    xy, length = map(int, input().split())
    if xy == 0:
        y_list.append(length)
    else:
        x_list.append(length)

x_list.sort() 
y_list.sort()

width = []
height = []

for i in range(1, len(x_list)):
    width.append(abs(x_list[i] - (x_list[i-1])))

for i in range(1, len(y_list)):
    height.append(abs(y_list[i] - (y_list[i-1])))

max_square = max(width) * max(height)

print(max_square)
