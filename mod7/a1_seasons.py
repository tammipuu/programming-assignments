seasons = (
    'talvi', 'talvi',
    'kevät', 'kevät', 'kevät',
    'kesä', 'kesä', 'kesä',
    'syksy', 'syksy', 'syksy',
    'talvi'
)

selection = int(input('Syötä kuukauden numero: '))
if selection >= 1 and selection <= 12:
    print(seasons[selection - 1])
else:
    print('Kuukausialueen ulkopuolella')