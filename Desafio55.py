#ler o peso de 5 pessoas e mostrar qual é o mais pesado e mais leve
maior = 0
menor = 0
for c in range(1, 6):
    p = float(input('Qual o Peso da {}° Pessoa: '.format(c)))
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi {}Kg'.format(menor))