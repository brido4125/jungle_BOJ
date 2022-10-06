sentence = list(map(str, input()))
explosion = input()
pop_times = len(explosion)
last_explosion = explosion[-1]
stack = []

for elem in sentence:
    stack.append(elem)
    # 폭발 문자열의 마지막 문자와 동일한 문자가 elem으로 나올 경우 stack에 폭발 문자열이 쌓였는지 체크
    if elem == last_explosion and ''.join(stack[-pop_times:]) == explosion:
        # 쌓여 있다면 pop 횟수 만큼 반복문 돌려서 폭발 문자열을 stack에 제외
        for i in range(pop_times):
            stack.pop(-1)


answer = ""
if not stack:
    print("FRULA")
else:
    for elem in stack:
        answer += elem
    print(answer)