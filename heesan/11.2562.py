list = []
for i in range(9):
    Num = int(input())
    list.append(Num)

Max = max(list)
print(Max)
print((list.index(Max)) + 1)
