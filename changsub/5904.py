N = int(input())

# print(len("m o o m o o o m o o"))
# print(len("m o o m o o o m o o m o o o o m o o m o o o m o o"))
sentence = "moo"
length = len(sentence)
cnt = 1
while length < N:
    sentence = sentence + "m" + ("o" * (cnt + 2)) + sentence
    length = len(sentence)
    print(length)

print(sentence[N - 1])
