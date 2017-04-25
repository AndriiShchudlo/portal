from pyramid.view import view_config
import sqlite3

@view_config(route_name='home', renderer='templates/home.pt')
def home(request):
    # MYSQL conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    conn = sqlite3.connect('mydb')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users')
    results = cursor.fetchall()
    print (results)
    for row in results:
        id = row[0]
        firstName=row[1]
        lastName=row[2]
    res = {
        'id':str(id),
        'first':firstName,
        'last':lastName,
    }
    print (firstName)
    conn.close()
    return res
