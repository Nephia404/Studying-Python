N,K = map(int,input().split())
A = list(map(int,input().split()))
Count = 0

for i in range(N):
    while (A[i] > K):
        A[i] = A[i]-1
        Count = Count + 1

print(Count)
