# tente adivinhar o numero q o pc sorteou
import random
from time import sleep
n = random.randrange(1, 6)
print('-=-'*20)
print('The Infinit chose you a number from 0-5. Try to guess the number: ')
u = int(input('Insert a Number and Try your Lucky: '))
print('LOADING...')
sleep(3)
print('-=-'*20)
if n == u:
    print('Wow! You Got It!')
else:
    print('Sorry even for this you are unlucky.')
    print('The number was {}.'.format(n))
