year = int(input('Syötä vuosi: '))

leap_year = False
if year % 4 == 0:
    leap_year = True
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year = True
        else:
            leap_year = False

if leap_year == True:
    print('Vuosi on karkausvuosi.')
else:
    print('Vuosi ei ole karkausvuosi.')