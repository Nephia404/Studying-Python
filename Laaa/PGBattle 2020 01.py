N = int(input())    #問題数入力
kekka = [input() for i in range(N)] #配列にコード提出したか入力
hukkin = 0

for i in range(N):  #問題数文繰り返し
    if kekka[i] == 'WA':
        hukkin = hukkin + 1
    elif kekka[i] == '-':
        hukkin = hukkin + 1
    else:
        pass

print(hukkin * 5)
