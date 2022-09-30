x, y = map(int, input().split())

thirty_one = [1,3,5,7,8,10,12]
thirty = [4,6,9,11]
twenty_eight = [2]

day_dic = {
    1: 'MON',
    2: 'THU',
    3: 'THU',
    4: 'SUN',
    5: 'TUE',
    6: 'FRI',
    7: 'SUN',
    8: 'WED',
    9: 'SAT',
    10: 'MON',
    11: 'THU',
    12: 'SAT',
}

days= ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

index = days.index(day_dic[x])
if y % 7 == 1:
    print(days[index])
if y % 7 == 2:
    if (index + 1) > 6:
        print(days[index + 1 - 7])
    else:
        print(days[index+1])
if y % 7 == 3: # 수
    if (index + 2) > 6:
        print(days[index + 2 - 7])
    else:
        print(days[index+2])
if y % 7 == 4:
    if (index + 3) > 6:
        print(days[index + 3 - 7])
    else:
        print(days[index+3])
if y % 7 == 5:
    if (index + 4) > 6:
        print(days[index + 4 - 7])
    else:
        print(days[index+4])
if y % 7 == 6:
    if (index + 5) > 6:
        print(days[index + 5 - 7])
    else:
        print(days[index+5])
if y % 7 == 0:
    if (index + 6) > 6:
        print(days[index + 6 - 7])
    else:
        print(days[index+6])

