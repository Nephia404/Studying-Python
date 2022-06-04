a,b,c = map(int,input().split())

if a>b:
    s = b
    b = a
    a = s

if b>c:
    s = c
    c = b
    b = s

if a>b:
    s = b
    b = a
    a = s

print(str(a)+' '+str(b)+' '+str(c))