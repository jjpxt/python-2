# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

opcao = 0

while opcao != 5:
    print(''' [ 1 ] somar
 [ 2 ] multiplicar
 [ 3 ] maior
 [ 4 ] novos números
 [ 5 ] sair do programa''')
    opcao = int(input('Qual sua opção? '))
    match opcao:
        case 1:
            print(f'{n1} + {n2} = {n1 + n2}')
            print('-=' *30)
        case 2:
            print(f'{n1} * {n2} = {n1 * n2}')
            print('-=' *30)
        case 3:
          if n1 > n2:
              print(f'{n1} é maior que {n2}')
          elif n1 == n2:
              print(f'{n1} é igual a {n2}')
          else:
                print(f'{n2} é maior que {n1}')
                print('-=' *30)
                print(' ')
        case 4:
            n1 = int(input('Novo primeiro número: '))
            n2 = int(input('Novo segundo número: '))
            print('-=' *30)


print('fim do programa. Volte sempre! ')