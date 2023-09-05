numbers = []

prog_input = input('Syötä luku: ')
while prog_input != '':
    numbers.append(int(prog_input))
    prog_input = input('Syötä luku: ')
    
numbers.sort(reverse = True)
nums_to_print = min(len(numbers), 5)
print('Luvut suurimmasta pienimpään:')
for f in range(nums_to_print):
    if f == nums_to_print - 1:
        print(numbers[f], end='')
    else:
        print(numbers[f], end=', ')
