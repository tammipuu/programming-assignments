length_in = 0
while True:
    length_in = float(input('Syötä pituus tuumissa: '))
    if length_in < 0:
        exit(0)
    print(f'Pituus senttimetreissä {length_in * 2.54:.2f} cm')