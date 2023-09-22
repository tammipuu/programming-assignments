import mysql.connector

def getAirportName(icao):
    cursor = cnx.cursor()
    query = 'SELECT name FROM airport'
    query += " WHERE ident='" + icao + "'"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    
    names = result[0]
    return names[0]

cnx = mysql.connector.connect(
    database = 'flight_game',
    user = 'root',
    password = 'salasana'
)

icao = input('Syötä lentokentän ICAO-koodi: ')
print(getAirportName(icao))

cnx.close()