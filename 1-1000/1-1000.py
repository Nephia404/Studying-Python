import random

randomNumbers = list(range(1000))

i = 0
number = 0
per = 0.0


for i in range(1000):
    randomNumbers[i] = random.randint(1,10)
    if i == 999:
        print("{0} ".format(randomNumbers[i]))
        continue
    print("{0} ".format(randomNumbers[i]), end="")


for i in range(1,11):
    number = randomNumbers.count(i)
    per = number / 1000
    print("{0}が現れた割合は{1}でした".format(i,per))
