import random

N = 8

dic = {
    1: "채도영",
    2: "이성준",  #
    3: "임준기",  #
    #4: "현어진",
    #5: "박범수",  #
    #6: "김언탁",  #
    #7: "권준현",  #
    4: "김헌우",  #
}

# count_dic = {
#     "채도영": 0,
#     "이성준": 0,  #
#     "임준기": 0,  #
#     "현어진": 0,
#     "박범수": 0,  #
#     "김언탁": 0,  #
#     "권준현": 0,  #
#     "김헌우": 0,  #
# }

random1 = random.randrange(1, 5)
random2 = random.randrange(1, 5)


print(dic[random1])
print(dic[random2])
#     print(dic[random1])
#     dic[random1] += 1
# print(dic[random2])
