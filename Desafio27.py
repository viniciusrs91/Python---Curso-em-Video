nome = str(input('Digite seu nome Completo: ')).strip()
separa = nome.split()
print('Seu Primeiro nome é: {}'.format(separa[0]))
print('Seu ultimo nome é: {}'.format(separa[len(separa)-1]))
