mass_leiviska = float(input('Anna massa leivisköissä: '))
mass_naula = float(input('Anna massa nauloissa: '))
mass_luoti = float(input('Anna massa luodeissa: '))

mass_naula += mass_leiviska * 20    # naulaa
mass_luoti += mass_naula * 32       # luotia
mass = mass_luoti * 13.3            # grammaa

print()
print(f'Massa on nykymitoissa {mass * 0.001:.1f} kilogrammaa ja {mass:.1f} grammaa.')