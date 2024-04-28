# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

numeros = cont = soma = 0
numeros = int(input('Digite um número [DIGITE 999 PARA PARAR]: '))
while numeros != 999:
    cont += 1
    soma += numeros
    numeros = int(input('Digite um número [DIGITE 999 PARA PARAR]: '))
print(f'Você digitou {cont} números, e a soma entre eles foi {soma}.')
