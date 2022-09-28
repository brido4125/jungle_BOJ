import sys
import time
start = time.time()

N = int(sys.stdin.readline())
words = []
for i in range(N):
    T = sys.stdin.readline().split()[0]
    words.append(T)

print(N)

set_words = set(words) # set으로 변환해서 중복값을 제거
set_words_listed = list(set_words) # 다시 list로 변환
set_words_listed.sort() # 알파벳 순으로 정렬
set_words_listed.sort(key=len) # 각 원소를 문자열의 길이 별로 정렬한다.

for i in set_words_listed:
    print(i)

print("time :", time.time() - start)
