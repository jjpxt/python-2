# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.


total = prod1000 = barato = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Qual produto? '))
    preço = float(input('Qual preço? R$ '))
    cont += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    total += preço
    if preço > 1000:
        prod1000 += 1
    resp = ' '
    while resp not in 'NS':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra é de {total:.2f}')
print(f'{prod1000} produtos custam mais de R$1000,00 reais.')
print(f'O produto {barato} é o mais barato e custa {menor:.2f} reais.')
