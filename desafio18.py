import math
#from math import radians, sin,cos,tan

a = int(input("Insert Angle: "))

s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))

print("The angle is: {}, Sine: {:.2f}, Cosine {:.2f}, Tangent {:.2f}".format(a,s,c,t))
