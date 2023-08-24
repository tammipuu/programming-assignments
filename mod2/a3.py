import math

base = float(input('Anna suorakulmion kanta (m):\t'))
height = float(input('Anna suorakulmion korkeus (m):\t'))

perimeter = 2 * (base + height)
area = base * height

print()
print(f'Suorakulmion piiri on {perimeter:.1f} m')
print(f'Suorakulmion pinta-ala on {area:.1f} m\u00b2')