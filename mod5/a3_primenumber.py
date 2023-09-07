integer = int(input('Syötä kokonaisluku: '))

is_prime = True
for f in range(2, integer - 1):
    if integer % (f + 1) == 0:
        is_prime = False
        break

if is_prime:
    print('Luku on alkuluku')
else:
    print('Luku ei ole alkuluku')