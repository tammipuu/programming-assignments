import math

def unitPrice(diameter, single_price):
    radius = diameter / 2
    area = math.pi * math.pow(radius, 2)
    unit_price = single_price / area
    return unit_price

print('Syötä ensimmäisen pizzan')
pizza1_diameter = float(input('- halkaisija: '))
pizza1_price = float(input('- hinta: '))
print('Syötä toisen pizzan')
pizza2_diameter = float(input('- halkaisija: '))
pizza2_price = float(input('- hinta: '))

pizza1_unit_price = unitPrice(pizza1_diameter, pizza1_price)
pizza2_unit_price = unitPrice(pizza2_diameter, pizza2_price)

print()
if pizza1_unit_price < pizza2_unit_price:
    print('Ensimmäinen pizza on halvin per yksikkö')
elif pizza2_unit_price < pizza1_unit_price:
    print('Toinen pizza on halvin per yksikkö')
elif pizza2_unit_price == pizza1_unit_price:
    print('Molemmat pizzat ovat samanhintaisia')