from random import randint

results = []

dice = int(input('Syötä arpakuutioiden määrä: '))
for f in range(dice):
    results.append(randint(1, 6))

print()
print('Silmälukujen summat:')
for f in range(len(results)):
    if f == len(results) - 1:
        print(results[f], end='')
    else:
        print(results[f], end=', ')