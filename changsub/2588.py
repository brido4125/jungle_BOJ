x = int(input())
y = int(input())


def get_targets(x):
    hundreds_mod = x % 100
    hundreds = x // 100
    tens = hundreds_mod // 10
    units = hundreds_mod % 10
    return hundreds, tens, units


x_targets = get_targets(x)
y_targets = get_targets(y)

answers = []

for i in range(2, -1, -1):
    answers.append(x * y_targets[i])

answers.append(x*y)

for x in answers:
    print(x)