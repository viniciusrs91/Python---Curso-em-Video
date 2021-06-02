# se 3 retas podem ou nao formar um triagulo
print('-='*20)
print('          TRIANGLE ANALYSE')
print('-='*20)
r1 = float(input('Enter the measure A: '))
r2 = float(input('Enter the Measure B: '))
r3 = float(input("Enter the Measure C: "))

if (r1 + r2) > r3 and (r1+r3) > r2 and (r2+r3) > r1:
    print("It's possible make a triangle with these measures.")
else:
    print("It's Not possible make a Triangle with these measures.")