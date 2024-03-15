x = int(input("Digite o valor do novo salário: R$"))

if x > 2000:
   x = x * 1.1
else:
   x *= 1.15
print('Novo salário é R$', x)