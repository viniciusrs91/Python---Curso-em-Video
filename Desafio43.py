print('Vamos Calcucar o seu IMC')
p = float(input('Digite seu PESO: '))
a = float(input('Digite Sua Altura: '))

imc = p /(a*a)

if imc <= 18.5:
    print('O seu IMC é de: {:.1f}, e esta ABAIXO do Recomendado.'.format(imc))
elif imc > 18.5 and imc <= 24.9:
    print('O sei IMC é de: {:.1f}, e está NORMAL.'.format(imc))
elif imc >= 25 and imc <= 29.9:
    print('O Seu IMC é de {:.1f}, e está ACIMA do normal.'.format(imc))
else:
    print('O Seu IMC é de {:.1f}, e é de OBESIDADE'.format(imc))