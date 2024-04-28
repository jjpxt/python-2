from datetime import date
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
# mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

#
# atual = date.today().year
# nasc = int(input('Qual seu ano de nascimento? '))
# idade = atual - nasc
#
# if idade <= 9:
#     print(f'Com {idade} anos, você é um ATLETA MIRIM')
# elif idade > 9 and idade <= 14:
#     print(f'Com {idade} anos, você é um ATLETA INFANTIL')
# elif idade > 14 and idade <= 19:
#     print(f'Com {idade} anos, você é um ATLETA JÚNIOR')
# elif idade > 19 and idade <= 25:
#     print(f'com {idade} anos, você é um ATLETA SÊNIOR')
# else:
#     print(f'com {idade} anos, você é um ATLETA MASTER')












atual = date.today().year
nasc = int(input('Qual seu ano de nascimento? '))
idade = atual - nasc

if idade <= 9:
    print(f' Com {idade} anos você é ATLETA MIRIM!')
elif idade <= 14:
    print(f' Com {idade} anos você é ATLETA INFANTIL!')
elif idade <= 19:
    print(f' Com {idade} anos você é ATLETA JUNIOR!')
elif idade <= 25:
    print(f' Com {idade} anos você é ATLETA SÊNIOR!')
else:
    print(f' Com {idade} anos você é ATLETA MASTER!')
