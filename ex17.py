# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sx = str(input('Qual seu sexo? [M/F]')).strip().lower()
while sx not in 'MmFf':
    sx = str(input('Sexo invalido. Digite apenas [M/F]')).strip().lower()
print(f'Sexo {sx} registrado com sucesso!')
