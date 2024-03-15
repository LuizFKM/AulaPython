x = int(input("Digite o valor do novo salário: R$"))

acrescimoUm = (x * 0.15) #acréscimo de 15% caso o salário seja até 2000
salarioNovoA = (x + acrescimoUm)
acrescimoDois = (x * 0.10) #acréscimo de 10% caso o salário seja até maior que 2000
salarioNovoB = (x + acrescimoDois)

if x <= 2000:
   print('Seu novo salário é: R$', int(salarioNovoA))
elif x > 2000:
   print("Seu novo salário é: R$", int(salarioNovoB))