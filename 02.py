a=int(input("digite seu ano de nascimento"))
b=int(input("digite o ano atual"))
idade=b-a
if idade>=18:
    print("Você tem", idade, "é maior de idade")
else:
    print("Você tem", idade, "é menor de idade")