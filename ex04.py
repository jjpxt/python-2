# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

n1 = int(input('Primeira nota: '))
n2 = int(input('Segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print(f'Sua média foi {media} REPROVADO')
elif media >= 5 and media <= 6.9:
    print(f'Sua média foi {media} RECUPERAÇÃO')
else:
    print(f'Sua média foi {media} APROVADO')
