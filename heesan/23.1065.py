# 어떤 양의 정수 X의 각자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.

# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성해라

# ex 110 99
# 1 1
# 210 105

# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
# 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

N = int(input())

count = 0


def Nunber_count(N):
    global count
    if N < 100:
        return N
    elif N == 1000:
        return 144
    else:
        for i in range(100, N+1):
            a = int(i // 100)
            b = int((i % 100) // 10)
            c = int(i % 10)
            if b-a == c-b:
                count = count + 1
        return (99 + count)


print(Nunber_count(N))
