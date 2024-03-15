x = int(input('Quantas horas ficou? '))

if x < 1:
     x = 1
else:
     valor = 7 + 4*(x-1)
print("Pagará R$", valor)