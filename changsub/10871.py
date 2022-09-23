N,X = map(int, input().split())

targets = list(map(int, input().split()))


for elem in targets:
    if X > elem:
        print(str(elem)+" ",end="")
