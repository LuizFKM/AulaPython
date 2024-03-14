x = int(input('Quantas horas ficou? '))

hora = x * 60
valorHora = 7 * x
horaExtra = (x*4)-4+7


if hora == 60:
    print('R$', valorHora)
elif hora > 60:
    print('R$', horaExtra)
