from random import randint
# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
print('     <<<< VAMOS JOGAR PAR OU ÍMPAR >>>>>')
v = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR OU ÍMPAR? [P/I] ')).strip().upper()
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('DEU PAR, VOCÊ VENCEU!')
            v += 1
        else:
            print('DEU ÍMPAR,VOCÊ PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('DEU ÍMPAR, VOCÊ VENCEU!')
            v += 1
        else:
            print('DEU PAR, VOCÊ PERDEU!')
            break
print(f'Game over, você venceu {v} vezes.')
