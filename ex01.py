# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = int(input('Qual valor da casa? '))
salario = int(input('Qual seu salário? '))
anos = int(input("Em quantos anos vai pagar o financiamento? "))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

if prestacao <= minimo:
    print('EMPRESTIMO APROVADO!')
else:
    print('EMPRESTIMO NEGADO!')
