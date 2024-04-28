from datetime import date

#  Crie um programa que leia o ano de nascimento de sete pessoas. No final,
#  mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
atual = date.today().year
maior = 0
menor = 0
for pess in range(1, 8):
    nasc = int(input(f"Que ano a {pess}ª pessoa nasceu? "))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} pessoas maior de idade.')
print(f'Ao todo tivemos {menor} pessoas maior de idade.')
