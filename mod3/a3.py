sex = input('Syötä sukupuolesi: ')
sex = sex.lower()
hemoglobin = int(input('Syötä hemoglobiiniarvosi (g/l): '))
hemoglobin_status = ''

if sex == 'mies' or sex == 'm':
    if hemoglobin < 134:
        hemoglobin_status = 'alhainen'
    elif hemoglobin > 195:
        hemoglobin_status = 'korkea'
    elif hemoglobin >= 134 and hemoglobin <= 195:
        hemoglobin_status = 'normaali'
if sex == 'nainen' or sex == 'n':
    if hemoglobin < 117:
        hemoglobin_status = 'alhainen'
    elif hemoglobin > 175:
        hemoglobin_status = 'korkea'
    elif hemoglobin >= 117 and hemoglobin <= 175:
        hemoglobin_status = 'normaali'

print('Sinulla on ' + hemoglobin_status + ' hemoglobiiniarvo.')