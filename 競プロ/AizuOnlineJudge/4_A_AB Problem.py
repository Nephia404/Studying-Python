a,b = map(int,input().split())
d=0
r=0
f=0

d = a // b
r = a % b
f = float(a / b) 

print(str(d)+' '+str(r)+' '+str(f))