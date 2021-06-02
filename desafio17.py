import math
import emoji
print(emoji.emojize(":triangular_ruler:HYPOTENUSA:triangular_ruler:"))
a = float(input("Insert Cateto oposto A: "))
b = float(input("Insert Cateto Adjacente B: "))
c = (a**2 + b**2) ** (1/2)
ca = math.hypot(a, b)

print ("The Hypotenuse of A: {}, and B: {} is equals {:.2f}".format(a,b,c))
print ("The Hypotenuse of A: {}, and B: {} is equals {:.2f}".format(a,b,ca))