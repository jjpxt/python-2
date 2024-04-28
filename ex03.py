from datetime import date
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou
# se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


atual = date.today().year
nasc = int(input('Nasceu em que ano? '))
idade = atual - nasc
print('-' * 80)

if idade == 18:
    print(f'quem nasceu em {nasc} tem {idade} anos, esse é o momento exato para se alistar!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Quem nasceu em {nasc}, tem {idade} anos, ainda faltam {saldo} anos para se alistar.')
elif idade > 18:
    saldo = idade - 18
    print(f'Quem nasceu em {nasc}, tem {idade} anos, ja deveria ter se alistado à {saldo} anos ')
