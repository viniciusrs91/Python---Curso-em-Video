frase = str(input('Digite a Frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]#pra escrever de tras pra frente
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Esta frase é um Palindromo!')
else:
    print('Esta frase não é um Palindromo.')