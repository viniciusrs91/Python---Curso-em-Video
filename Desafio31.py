#distancia da viagem, se maior que 200km tem disconto
km = float(input('Qual a Distância da Viagem? '))
if km <= 200:
    print('O total da sua viagem será: ${:.2f}'.format(km*0.50))
else:
    print('O Total da Sua Viagem Será: ${:.2f}'.format(km*0.45))

#if simplificado
#preço = km * 0.50 if km <= 200 else km * 0.45
#print('O total da viagem será de ${:.2f}'.format(preço))