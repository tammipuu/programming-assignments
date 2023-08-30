largest_number = None
smallest_number = None
program_input_float = 0

program_input = input('Syötä luku: ')
while program_input != '':
    program_input_float = float(program_input)
    
    if smallest_number == None or program_input_float < smallest_number:
        smallest_number = program_input_float
    
    if largest_number == None or program_input_float > largest_number:
        largest_number = program_input_float
    
    program_input = input('Syötä luku: ')

print()
print(f'Pienin luku: {smallest_number:.2f}')
print(f'Suurin luku: {largest_number:.2f}')