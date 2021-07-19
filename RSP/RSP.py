import random

print('グー:0 チョキ:1 パー:2 疲れた:3')
man = int(input())

while man != 3:
    com = random.randint(0, 2)

    kekka = 0
    kekka = (man-com+2) % 3
    if kekka == 2:
        hantei = "あいこ"
    elif kekka == 1:
        hantei = "勝ち"
    else:
        hantei = "負け"

    t_flg = 0
    t_save = [0] * 2
    n_save = [0] * 2

    t_save[0] = com
    t_save[1] = man

    while t_flg <= 1:
        if t_save[t_flg] == 0:
            n_save[t_flg] = "グー"
            break
        elif t_save[t_flg] == 1:
            n_save[t_flg] = "チョキ"
            break
        else:
            n_save[t_flg] = "パー"
            break
    t_flg = t_flg + 1

    print("コンピュータ:{0} 自分:{1}".format(n_save[0], n_save[1]))
    print(hantei)

    print('グー:0 チョキ:1 パー:2 疲れた:3')
    man = int(input())