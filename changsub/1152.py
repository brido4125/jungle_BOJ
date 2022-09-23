s = input()
split = s.split(" ")
count = 0
for x in split:
    if x == '':
        count += 1


print(len(split)-count)
