# -*- coding: utf-8 -*-

price = float(raw_input('podaj wartość produktu > '))

print("""
    1 - 0%
    2 - 5%
    3 - 8%
    4 - 18%
    5 - 23%
""")

vat_gr = int(raw_input('podaj grupę VAT > '))
vat_val = 0

if vat_gr == 1:
    vat_val = 0
elif vat_gr == 2:
    vat_val = 0.05
elif vat_gr == 3:
    vat_val = 0.08
elif vat_gr == 4:
    vat_val = 0.18
elif vat_gr == 5:
    vat_val = 0.23
else:
    vat_val = 0

price_vat = price * vat_val

print("Podatek VAT od wprowadzonego towaru wynosi " + str(price_vat))
