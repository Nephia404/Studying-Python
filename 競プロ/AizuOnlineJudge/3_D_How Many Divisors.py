a,b,c = map(int, input().split())   #3つの変数に標準入力
count = 0                           #count初期化
for i in range(a,b+1):              #aからbまでの数をiに入れて繰り返し
        if c % i == 0:                  #iがc約数だった時
            count = count + 1           #カウントを増やす

print(count)
