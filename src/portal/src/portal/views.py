from pyramid.view import view_config
import sqlite3
from pyramid.response import Response

@view_config(route_name='home', renderer='templates/home.pt')
def home(request):
    # MYSQL conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    conn = sqlite3.connect('mydb')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users')
    results = cursor.fetchall()
    print (results)




    conn.close()
    return {'user': results}