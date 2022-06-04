a,b = map(int,input().split())

d = a // b
r = a % b
f = float(a / b) 

print(str(d)+' '+str(r)+' '+str(round(f,5)))