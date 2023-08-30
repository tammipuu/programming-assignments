from getpass import getpass

set_username = 'python'
set_password = 'rules'

while True:
    username = input('Käyttäjätunnus: ')
    password = getpass('Salasana: ')
    if username == set_username and password == set_password:
        print('Tervetuloa')
        break
    else:
        print('Pääsy evätty')