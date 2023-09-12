def getOddNumbers(numbers):
    evenNumbers = []
    for number in numbers:
        if number % 2 == 0: # jos parillinen
            evenNumbers.append(number)
    return evenNumbers

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
strippedList = getOddNumbers(originalList)
print()
print(f'Alkuperäinen:\t{originalList}')
print(f'Karsittu:\t{strippedList}')