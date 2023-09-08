from random import randint

def throwDice():
    return randint(1, 6)

dice_throws = []
dice = 0
while (dice != 6):
    dice = throwDice()
    dice_throws.append(dice)

throw_amount = len(dice_throws)
if throw_amount != 1:
    print(f'Sain silmäluvuksi numerot ', end='')
    for id, throw in enumerate(dice_throws):
        if id == throw_amount - 1:
            print(f'ja {throw}')
        elif id == throw_amount - 2:
            print(f'{throw} ', end='')
        else:
            print(f'{throw}, ', end='')
else:
    print(f'Sain silmäluvuksi numeron ', end='')
    print(dice_throws[0])
