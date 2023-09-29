import math

a = float(input("Введите 1: "))
b = float(input("Введите 2: "))

z1 = ((math.cos(a)-math.cos(b))** 2) - ((math.sin(a)-math.sin(b))**2)
print ("Z1: " , z1)
#z2 = (-4 * math.sin((a -b)/ 2)) * math.cos(a + b)
z4 = (a + b)
z2 = (a - b) / 2

z3 = (-4 * (math.sin(z2)**2)) * math.cos(z4)
print ("Z2: " , z3)
