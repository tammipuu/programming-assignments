minimum_length = 37
length = float(input('Syötä kuhan pituus (cm): '))
missing_length = minimum_length - length

if length < minimum_length:
    print(f'Kuha on alamittainen. Alimmasta sallitusta pyyntimitasta puuttuu {missing_length:.1f} cm. Laske se takaisin järveen.')
else:
    print('Kuha on normimittainen.')