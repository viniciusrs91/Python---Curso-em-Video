#Multa por exesso de velocidade
km= int(input('Qual a Velocidade da Nave? '))

if km >=80:
    vm = (km - 80)*7
    print('Voce foi multado $7 por KM excedido: ${}'.format(vm))
else:
    print('Obrigado por respeitar o Limite.')
print('Bom dia')