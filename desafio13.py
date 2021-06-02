# Salary Raise 15%

sal= float(input('Insert Actual Salary: $'))
#r= float ((sal*0.15)+sal) NAO FUNCIONA PRA TODA PORCENTAGEM
r= sal + (sal * 15 / 100)

print ('Your preview salary was: $ {:.2f}'.format(sal))
print ('Your new Salary is: $ {:.2f}'.format(r))