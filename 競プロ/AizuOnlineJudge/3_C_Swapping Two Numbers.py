li_1 = []               # => 空のリストを定義
li_2 = []

a,b = map(int,input().split())

while True:                         #無限ループ
    if a == 0 and b == 0:           #入力値が0 0の時
        break                       #処理終了
    else:                           #それ以外の時
        if a > b:                   #aがbより大きい時
            a,b=b,a                 #a,bの中身を入れ替え(一時的な変数がいらない)
        li_1.append(a)              #配列li_1の最後尾に左の値追加
        li_2.append(b)              #配列li_2の最後尾に右の値追加
    a,b = map(int,input().split())  #再度値入力

for i in range(len(li_1)):                  #二つの配列を頭から順番に表示
    print(str(li_1[i])+' '+str(li_2[i]))    