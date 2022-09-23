target = 1
for x in list(int(input()) for _ in range(3)):
    target *= x

dic = {}

target = str(target)

for i in range(len(target)):
    key = target[i]
    if key in dic:
        dic[key] += 1
    else:
        dic[key] = 1

answers = [0] * 10
for key in dic.keys():
    answers[int(key)] = dic[key]

for answer in answers:
    print(answer)