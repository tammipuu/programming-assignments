airports = {}

def addAirport():
    ap_icao_code = input('Syötä ICAO-koodi: ')
    ap_icao_code = ap_icao_code.upper()
    if ap_icao_code == '':
        print('Koodia ei syötetty, lopetetaan')
    else:
        ap_name = input('Syötä nimi: ')
        airports[ap_icao_code] = ap_name
        print('Lentoasema lisätty')
    print()
    return

def searchAirport():
    ap_icao_code = input('Syötä ICAO-koodi: ')
    ap_icao_code = ap_icao_code.upper()
    if ap_icao_code == '':
        print('Koodia ei syötetty, lopetetaan')
    elif ap_icao_code in airports:
        print('Listalta löytyi kohde:')
        print(f'{ap_icao_code}, {airports[ap_icao_code]}')
    else:
        print('Lentokenttää ei löytynyt sanakirjasta.')
    print()
    return

while True:
    selection = input('Haluatko lisätä uuden lentoaseman tai hakea tallennettua lentoasemaa? [lisää, hae, lopeta] ')
    if selection == 'lisää':
        addAirport()
    elif selection == 'hae':
        searchAirport()
    elif selection == 'lopeta':
        break
