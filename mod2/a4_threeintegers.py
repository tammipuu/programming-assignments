int1 = int(input('Anna 1. kokonaisluku: '))
int2 = int(input('Anna 2. kokonaisluku: '))
int3 = int(input('Anna 3. kokonaisluku: '))

sum = int1 + int2 + int3
product = int1 * int2 * int3
mean = (int1 + int2 + int3) / 3

print()
print('Lukujen summa on ' + str(sum))
print('Lukujen tulo on ' + str(product))
print(f'Lukujen keskiarvo on {mean:.2f}')