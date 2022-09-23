num = int(input())


# num은 1~1000 사이
def is_hansu(num):
    # 한자리수 or 두자리 수는 무조건 한수
    if num < 100:
        return True
    hundres = num // 100
    hundres_mod = num % 100
    tens = hundres_mod // 10
    units = hundres_mod % 10
    if hundres - tens == tens - units:
        return True
    return False


answer = 0
for i in range(1, num + 1):
    if is_hansu(i):
        answer += 1

print(answer)
