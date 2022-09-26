N = int(input())

for i in range(N):
    num, text = input().split()
    result = ''
    for i in text:
        result = result + int(num) * i
    print(result)
