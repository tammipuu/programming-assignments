def convert(gallons):
    liters = gallons * 3.785
    return liters

amount_gal = float(input('Syötä bensiinin määrä gallonoina: '))
amount_ltr = convert(amount_gal)
print(f'Määrä litroina: {amount_ltr:.2f}')