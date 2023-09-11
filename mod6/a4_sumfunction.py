def sum(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

numbers = [6, 9, 4, 1]
print(f'Lukujen summa: {sum(numbers)}')