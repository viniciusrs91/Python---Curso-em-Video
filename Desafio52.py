n = int(input('Digite um número: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[31m', end='')
        tot += 1
    else:
        print('\033[34m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi dividido {} vezes'.format(n, tot))
if tot == 2:


    print('\033[31mE por isso ele È PRIMO')
else:
    print('\033[34mE por isso ele NÃO é PRIMO')