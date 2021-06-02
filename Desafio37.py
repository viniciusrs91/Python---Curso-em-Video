num = int(input('Digite um numero INTEIRO: '))
print('''Escolha uma Base de Conversão:
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')

op = int(input('Sua Opção: '))

if op == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif op ==2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif op ==3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num,hex(num)[2:]))
else:
    print('Opção Invalida, nao sabe Ler? ')