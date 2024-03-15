print('Digite o tamanho dos três lados do triangulo e descubra seu tipo')
ladoA = int(input('Digite o primeiro lado: '))
ladoB = int(input('Digite o segundo lado: '))
ladoC = int(input('Digite o terceiro lado: '))

if ladoA == ladoB and ladoA == ladoC:
    print('Triangulo equilátero!')
elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
    print('Triangulo isóceles!')
else:
    print('Triangulo escaleno!')
