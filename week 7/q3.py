"""writing a program to output the jersey number of the player
player name given in player.txt
"""

import os
import sys
import psycopg2

file = open('players.text', 'r')
name = file.read()

try:
    connection = psycopg2.connect(
        database = sys.argv[1],
        password = os.environ.get('PGPASSWORD'),
        user = os.environ.get('PGUSER'),
        port = os.environ.get('PGPORT'),
        host = os.environ.get('PGHOST')
    )

    cursor = connection.cursor()
    query = 'SELECT jersey_no from players where name = {}'.format(name)
    cursor.execute(query)

    result = cursor.fetchall()

    for res in result:
        print(res[0])
    cursor.close()
except (Exception, psycopg2.DatabaseError) as e:
    print(e)
finally:
    connection.close
