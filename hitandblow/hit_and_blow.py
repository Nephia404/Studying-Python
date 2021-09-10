import random

color_list = ["red","blue","yellow","purple","green"]

random.shuffle(color_list)

answer_list = list(range(4))

hit = 0
blow = 0
i = 0
for i in [0,1,2,3]:
    answer = color_list[i]
    answer_list[i] = answer

while hit != 4:
    i = 0
    answer_input = []
    for i in [0,1,2,3]:
        answer = input(str(i+1) +'個目の答えを入力してください:')
        while answer in answer_input:
                answer = input("違う色を入力してください。")
        answer_input.insert(i,answer)
    
    i = 0
    n = 0
    hit = 0
    blow = 0
    for i in [0,1,2,3]:
        for n in [0,1,2,3]:
            if answer_input[i] == answer_list[n] and i == n:
                hit = hit + 1
            elif answer_input[i] == answer_list[n]:
                blow = blow + 1
    print(str(hit) + "ヒットです。")
    print(str(blow) + "ブローです。\n")

else:
    print("正解です。")
    input()
