from time import sleep
from datetime import date

ano = date.today().year
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('Happy {}!'.format(ano))