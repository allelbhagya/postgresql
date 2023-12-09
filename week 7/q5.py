import os
import sys
import psycopg2

file = open('team.txt', 'r')
id = file.read()


try:
    connection = psycopg2.connect(
        database = sys.argv[1],
        user = os.environ.get('PGUSER'),
        password = os.environ.get('PGPASSWORD'),
        host = os.environ.get('PGHOST'),
        port = os.environ.get('PGPORT')
    )

    cursor = connection.cursor()
    query = "select playground from teams where team_id = '{}'".format(id)
    cursor.execute(query)
    result = cursor.fetchall()
    for res in result:
        print(res[0])
    cursor.close()
except(Exception, psycopg2.DatabaseError) as e:
    print(e)
finally:
    connection.close