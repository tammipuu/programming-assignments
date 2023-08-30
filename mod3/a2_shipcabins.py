answer = input('Mistä hyttiluokasta haluat tietoa? ')
answer = answer.lower()
if answer == 'lux':
    print('LUX on parvekkeellinen hytti yläkannella.')
elif answer == 'a':
    print('A on ikkunallinen hytti autokannen yläpuolella.')
elif answer == 'b':
    print('B on ikkunaton hytti autokannen yläpuolella.')
elif answer == 'c':
    print('C on ikkunaton hytti autokannen alapuolella.')
else:
    print('Virheellinen hyttiluokka')