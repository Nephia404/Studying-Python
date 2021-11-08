P = int(input())
P = P / 100
L = 1 - P
Ans = 0.0

Ans = P*P*P*P*L*L*L
Ans = Ans + P*P*P*P*P*L*L
Ans = Ans + P*P*P*P*P*P*L
Ans = Ans + P*P*P*P*P*P*P

print(Ans)

