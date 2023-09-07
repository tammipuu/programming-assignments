cities = []

print('Syötä viisi kaupungin nimeä.')
for f in range(5):
    cities.append(input(f'{f + 1}: '))

print()
for city in cities:
    print(city)