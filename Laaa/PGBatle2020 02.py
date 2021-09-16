N = int(input())
Number = str(2**N)
Zero ='0.'

for i in range(N-1):
    Zero = Zero + '0'

print(Zero+Number)