sentence = input()

numbers = []
opers = []

target = ''
for i in sentence:
    if i == '-':
        opers.append(i)
        numbers.append(int(target))
        target = ''
    elif i == '+':
        opers.append(i)
        numbers.append(int(target))
        target = ''
    else:
        target += i

numbers.append(int(target))

minus_index = None

for i in range(len(opers)):
    if opers[i] == '-':
        minus_index = i + 1
        break

answer = 0

if minus_index is None:
    answer = sum(numbers)
else:
    for i in range(len(numbers)):
        if i >= minus_index:
            answer -= numbers[i]
        else:
            answer += numbers[i]

print(answer)