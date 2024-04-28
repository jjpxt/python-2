# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

preço = float(input('Qual o preço? R$ '))
forma_pg = int(
    input('Forma de pagamento:\n[1] - A VISTA DINHEIRO/ CHEQUE = 10% DE DESCONTO \n[2] - A VISTA NO CARTÃO = '
          '5% DE DESCONTO\n'
          '[3] - EM 2 VEZES = MESMO VALOR\n[4] - 3 OU MAIS VEZES =  20% DE JUROS\n'))

if forma_pg == 1:
    preço = preço - (preço * 10 / 100)
    print(f'Você ganhou 10% de desconto, o novo valor será de R$ {preço:.2f} reais.')
elif forma_pg == 2:
    preço = preço - (preço * 5 / 100)
    print(f'Você ganhou 5% de desconto, o novo valor será de R$ {preço:.2f} reais.')
elif forma_pg == 3:
    print(f'Voce parcelou a compra em 2 vezes, o valor sera de R$ {preço:.2f} reais.')
elif forma_pg == 4:
    if forma_pg == 4:
        perg = int(input('Em quantas vezes quer parcelar? '))
    preço = preço + (preço * 20 / 100)
    par = preço / perg
    print(f'Você parcelou em {perg} vezes, com 20% de juros o valor passará a ser de R$ {preço:.2f} reais,\n'
          f'e cada parcela irá ser de R$ {par:.2f} reais.')
else:
    forma_pg = 0
    print('OPÇÃO DE PAGAMENTO INVALIDA!')