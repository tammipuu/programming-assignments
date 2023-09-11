def removeOddNumbers(numbers):
    for id, number in enumerate(numbers):
        print(f'id = {id}')
        if number % 2: # jos pariton
            print('pariton löytyi')
            del numbers[id]
    return numbers

# kysytään kokonaislukuja
originalList = []
print('Syötä kokonaislukuja. (lopeta tyhjällä)')
list_index = 1

text_input = input(f'{list_index}: ')
while text_input != '':
    try:
        int_input = int(text_input)
        originalList.append(int_input)
        list_index += 1
    except ValueError:
        print('Virheellinen syöte')
    text_input = input(f'{list_index}: ')

# annetaan lista funktiolle, joka poistaa parittomat luvut
strippedList = removeOddNumbers(originalList)
print(strippedList)