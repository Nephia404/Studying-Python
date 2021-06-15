year = input("input year:")

y = int(year)

if (y % 400 == 0):
    print("閏年です。")
elif (y % 100 == 0):
    print("not閏年です。")
elif (y % 4 == 0):
    print("閏年です。")
else:
    print("not閏年です。")
input()