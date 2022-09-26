# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

# 예제 입력 1
# 4
# 1 3 5 7
# 예제 출력 1
# 3



test_number = int(input())
numbers = map(int, input().split())

sosunumber = 0
def check_sosu(x):
    notsosu = 0
    oksosu = 0
    if x==1:
        oksosu =0
    else:
        for i in range(2,x-1):
            if x % i == 0:
                notsosu += 1
        if notsosu > 0:
            oksosu = 0
        else:
            oksosu = 1
    return oksosu

for number in numbers:
    sosunumber += check_sosu(number)

print(sosunumber)