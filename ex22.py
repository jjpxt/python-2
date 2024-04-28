# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

# numero = cont = soma = 0
# numero = int(input('Digite um numero: '))
# while numero != 999:
#     cont += 1
#     soma += numero
#     numero = int(input('Digite um numero: '))
# print(f'Foram digitados {cont} numeros.')
# print(f'E a soma deles é de {soma}')


numero = cont = soma = 0
while True:
    numero = int(input('Digite um numero: '))
    if numero == 999:
        break
    cont += 1
    soma += numero
print(f'Foram digitados {cont} numeros.')
print(f'E a soma deles é de {soma}')

