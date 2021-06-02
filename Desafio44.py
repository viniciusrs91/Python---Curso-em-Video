val = float(input('Valor a ser Pago R$: '))
forma = int(input('=====Forma de Pagamento======\n1 - Á VISTA: Cheque/Dinheiro'
                  ' \n2 - Á VISTA: Cartão \n3 - 2X Cartão \n4 - 3X ou Mais\nFORMA: '))

if forma == 1:
    dezp = val - (val * 0.10)
    print('Á VISTA você tem 10% OFF, de R$ {:.2f} sua compra foi para R$ {:.2f}.'.format(val, dezp))
elif forma == 2:
    cincop = val - (val*0.05)
    print('Á Vista no Cartão você tem 5%O FF, de R$ {:.2f} sua compra foi para R$ {:.2f}.'.format(val, cincop))
elif forma == 3:
    print('Á sua Valor da Sua compra é de R$ {:.2f} sem Juros.'.format(val))
elif forma == 4:
    vintep = val + (val*0.2)
    print('Á Sua compra tem juros de 20% de R$ {:.2f} para R$ {:.2f}.'.format(val, vintep))