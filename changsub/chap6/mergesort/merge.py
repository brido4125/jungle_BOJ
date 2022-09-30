# 정렬을 마친 두 배열을 병합하기

from typing import Sequence, MutableSequence


def merge_sorted_list(a: Sequence, b: Sequence, c: MutableSequence) -> None:
    pa, pb, pc = 0, 0, 0  # 각 배열의 현재 위치를 나타내는 커서
    na, nb, bc = len(a), len(b), len(c),

    while pa < na and pb < nb:
        if a[pa] <= b[pb]:
            c[pc] = a[pa]
            pa += 1  # a 배열에 원소를 추가했으니 커서를 하나 증가
        else:
            c[pc] = b[pb]
            pb += 1
        pc += 1  # 결과 배열 또한 인덱스가 추가 되었으니 커서 인덱스 하나 증가

    # 만얀 A배열에 원소가 남아 있으면
    while pa < na:
        c[pc] = a[pa]
        pa += 1
        pc += 1

    # 만얀 A배열에 원소가 남아 있으면
    while pb < nb:
        c[pc] = b[pa]
        pb += 1
        pc += 1


if __name__ == '__main__':
    a = [2, 4, 6, 8, 11, 13]
    b = [1, 2, 3, 4, 9, 16, 21]
    c = [None] * (len(a) + len(b))
    print("주어진 두 배열의 병합 수행")

    merge_sorted_list(a,b,c)
    print(f'배열 a : {a}')
    print(f'배열 b : {b}')
    print(f'배열 c : {c}')
