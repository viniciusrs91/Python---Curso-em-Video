# Insert High and wide of wall

a = float(input('Insira a Altura da Parede: '))
l = float(input('Insira a Largura: '))

ar = float (a*l)
t = float (ar/2)

print('Sua parede tem a dimensão de {} X {} e sua área é de {}m².\nSerão necessarios {} litros de tinta.'.format(a,l,ar,t))