valor = float(input('Qual o valor da sua compra? '))
qtd = int(input('Quantos ítens são? '))




if qtd <= 5:
    desconto = valor * 0.05
elif qtd <= 14:
    desconto = valor * 0.10
else:
    desconto = valor * 0.15

print('Valor da Compra..> R$ ', valor)
print('Valor do desconto..> R$ ', desconto)
print('Valor da Compra..> R$ ', valor-desconto)