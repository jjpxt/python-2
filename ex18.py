# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint

computador = randint(1, 10)

print('Escolha um número de 1 até 10 e veja se é o mesmo número que eu pensei.')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
print(f'Você acertou o número que eu pensei com {palpite} tentativas.')
