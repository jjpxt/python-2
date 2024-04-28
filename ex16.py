# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
somaidade = 0
mediaidade = 0
maioridadeH = 0
nomevelho = 0
mulher = 0
for p in range(1, 5):
    print(f'------- {p}ª PESSOA -------')
    nome = input('Qual seu nome: ').strip()
    idade = int(input('Quantos anos você tem? '))
    sexo = input('Qual seu sexo? [M/F]').strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadeH = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeH:
        maioridadeH = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher += 1

mediaidade += somaidade / 4
print(f'a media de idade do grupo é de {mediaidade} anos')
print(f'O homem mais velho se chama {nomevelho} e tem {maioridadeH} anos')
print(f'Ao todo são {mulher} mulher(es) com menos de 20 anos.')
