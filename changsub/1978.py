N = int(input())
answer = list(map(int, input().split()))


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


count = 0
for elem in answer:
    if is_prime(elem):
        count += 1

print(count)
