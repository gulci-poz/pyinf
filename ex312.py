# -*- coding: utf-8 -*-

# w py3 mamy input zamiast raw_input()
number1 = int(input('podaj pierwszą liczbę > '))
number2 = int(input('podaj drugą liczbę > '))

# używając przecinka (lub formatowania) nie trzeba się martwić konkatenacją stringów
# w przypadku py2 przecinek w print() da nam wydruk w postaci tuple
print("Suma: %d" % (number1 + number2))
