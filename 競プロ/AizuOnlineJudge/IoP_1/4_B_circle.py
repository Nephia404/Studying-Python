import math #mathライブラリを利用する

r = float(input())
menseki=round(r*r*math.pi,6)
enshu=(round(2*r*math.pi,6))

print("{} {}".format(menseki,enshu))