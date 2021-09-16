x = int(input())
h = x // 3600           #[//]で整数だけの割り算ができる。
m = (x % 3600) // 60
s = (x % 3600) % 60
print(str(h)+':'+str(m)+':'+str(s))