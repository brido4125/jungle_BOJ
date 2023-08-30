def getCoordination(line1, line2):
    A, B, E = line1
    C, D, F = line2
    mother = (A * D - B * C)
    if mother != 0:
        mod1 = (B * F - E * D) % mother
        mod2 = (E * C - A * F) % mother
        if mod1 == 0 and mod2 == 0:
            return (int((B * F - E * D) / mother), int((E * C - A * F) / mother))

    return None


def solution(line):
    answer = []
    N = len(line)
    x_max = y_max = -int(1e15)
    x_min = y_min = int(1e15)
    cord_int = []

    for i in range(N):
        for j in range(i + 1, N):
            res = getCoordination(line[i], line[j])
            if res != None:
                x_max, y_max = max(res[0], x_max), max(res[1], y_max)
                x_min, y_min = min(res[0], x_min), min(res[1], y_min)
                cord_int.append(res)

    x_len = x_max - x_min + 1
    y_len = y_max - y_min + 1
    cord = [['.'] * x_len for _ in range(y_len)]
    for x, y in cord_int:
        if x_min < 0:
            nx = x + abs(x_min)
        else:
            nx = x - x_min
        if y_min < 0:
            ny = y + abs(y_min)
        else:
            ny = y - y_min
        cord[ny][nx] = '*'
        print(x, y)
        print(nx, ny)
    for result in cord:
        answer.append(''.join(result))

    return answer[::-1]