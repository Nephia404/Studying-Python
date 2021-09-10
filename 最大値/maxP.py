import random

random_list = [0]*20
hai2 = [0]*20

for i in range(20):
    random_list[i] = random.randint(1,51)
print(random_list)


maxP = 0
for j in range(20):
    for i in range(20):
        if random_list[maxP] < random_list[i]:
            maxP = i
    hai2[j] = random_list[maxP]
    random_list[maxP] = 0

print("narabikae",str(hai2))
