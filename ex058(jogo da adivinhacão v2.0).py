import random
comp = random.randint(0,10)
print('vou pensar em número de 1 a 10 tente adivinhar:')
acertou = False
cont = 0
while not acertou:
    jogador = int(input('Digite um número de 1 a 10:'))
    cont += 1
    if jogador != comp:
        print('errou!!! Digite um número de 1 a 10:')
    elif jogador == comp:
        print('Parabens, eu realmente escolhi {}\n'
              'Você acertou com {} tentativas'.format(comp,cont))
        acertou = True

