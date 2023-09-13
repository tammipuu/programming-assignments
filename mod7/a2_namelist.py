last_inputs = set()
in1 = input('Syötä nimi: ')
while in1 != '':
    # Käy nimilista läpi ja määrittele, onko aiemmin syötetty
    last_name = False
    for name in last_inputs:
        if in1 == name:
            last_name = True
            break
    if last_name == True:
        print('Aiemmin syötetty nimi')
    else:
        print('Uusi nimi')
    
    last_inputs.add(in1)
    in1 = input('Syötä nimi: ')

print()
print('Syötetyt nimet:')
print(last_inputs)