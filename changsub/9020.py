N = int(input())

prime_list = []  # 체를 통해 걸러진 소수를 담는 리스트


def prime_by_eratosthenes(primes):
    check = [0] * (10000 + 1)
    check[0] = 1
    check[1] = 1  # 0과 1은 소수에서 제외
    for i in range(2, len(check)):
        if check[i] == 0:
            primes.append(i)
            for j in range(2 * i, len(check), i):
                check[j] = 1
    return check


check = prime_by_eratosthenes(prime_list)
for _ in range(N):
    target = int(input())
    answers = []
    abs_list = []
    min_val = 100000

    for elem in prime_list:
        priv = elem
        compare = target - elem
        if compare + elem == target and check[compare] == 0:
            if min_val > abs(elem - compare):
                min_val = abs(elem - compare)
            answers.append((elem, compare))
            abs_list.append(abs(elem - compare))

    # 골드바흐 파티션의 갯수가 짝수인 경우 반으로 나눠서 가짓 수 줄이기
    if len(answers) % 2 == 0:
        answers = answers[:len(answers) // 2]
        abs_list = abs_list[:len(abs_list) // 2]
        index = 0
        for i in range(len(abs_list)):
            if abs_list[i] == min_val:
                index = i
        print(answers[index][0], answers[index][1])
    else:  # 파티션의 갯수가 홀수 => 동일한 소수의 합으로 이루어지 파티션이 존재, 해당 파티션의 차이는 무조건 0이므로 바로 정답 출력
        mid_index = (len(answers) - 1) // 2
        print(answers[mid_index][0], answers[mid_index][1])
