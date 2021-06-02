num = str(input('Insert a Number from 0 - 9999: '))
uni = num[3:]
dez = num[2:3]
cen = num[1:2]
mil = num[0:1]

print("Analizando o Número: {}.".format(num))

print("""Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}""".format(uni,dez,cen,mil))

