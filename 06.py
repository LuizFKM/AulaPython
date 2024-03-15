x = int(input('Qual o valor da sua compra? '))
y = int(input('Quantos ítens são? ')
        )
cincoItens = x * 0.05
seisAteQuatorze = x * 0.10
quinzeItens = x * 0.15
precoUm = x - cincoItens
precoDois = x - seisAteQuatorze
precoTres = x - quinzeItens



if y <= 5:
    print("O valor com desconto fica: R$", precoUm)
elif y > 5 and y <= 14:
    print("O valor com desconto fica: R$", precoDois)
else:
    print('O valor com desconto fica: R$', precoTres)