x,y = map(str,input().split())
reversed_x = x[::-1]
reversed_y = y[::-1]
if int(reversed_x) > int(reversed_y):
    print(reversed_x)
else:
    print(reversed_y)

