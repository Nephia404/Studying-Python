x=[]
n = int(input())        #0入力で終わりにしたい為、先に一回目入力
while n != 0:
    x.append(n)         #配列xの最後尾に入力したnを追加していく
    n = int(input())    #次の数を入力する

for i in range(len(x)):
    print('case '+str((i+1))+': '+str(x[i]))