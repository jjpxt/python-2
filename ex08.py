# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0,2)
print('PEDRA [1]\nPAPEL [2]\nTESOURA [3]')
print('-=' * 18)
jogador = int(input('          Qual sua jogada? '))
print('-=' * 18)
print(f'    O computador escolheu {itens[pc]}')
print('-=' * 18)
print(f'      Jogador escolheu {itens[jogador]}')
print('xXx' * 15)
print()
if pc == 0:  #PEDRA
    if jogador == 0:
        print('             EMPATOU')
    elif jogador == 1:
        print('              JOGADOR VENCEU!')
    elif jogador == 2:
        print('           COMPUTADOR VENCEU!')
    else:
        print('           JOGADA INVALIDA!')
elif pc == 1: #PAPEL
    if jogador == 0:
        print('            COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('             EMPATOU!')
    elif jogador == 2:
        print('                JOGADOR VENCEU!')
    else:
        print('                 JOGADA INVALIDA!')
elif pc == 2: #TESOURA
    if jogador == 0:
        print('                JOGADOR VENCEU!')
    elif jogador == 1:
        print('                  COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('             EMPATE!')
    else:
        print('               JOGADA INVALIDA!')
