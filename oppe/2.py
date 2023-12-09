import os
import sys
import psycopg2

file = open('date.txt', 'r')
date = file.read()

try:
    connection = psycopg2.connect(
        database = sys.argv[1],
        user = os.environ.get('PGUSER'),
        password = os.environ.get('PGPASSWORD'),
        host = os.environ.get('PGHOST'),
        port = os.environ.get('PGPORT')
    )

    cursor = connection.cursor()

    query ="select referees.name from referees, match_referees, matches where matches.match_date = '{}' and matches.match_num = match_referees.match_num and match_referees.referee = referees.referee_id".format(date)
    cursor.execute(query)
    result_of_query = cursor.fetchall()
    for result in result_of_query:
        list_of_name = list(map(str, result[0].split(" ")))
        final_result = list_of_name[-1]
        for name in list_of_name[:-1]:
            final_result += " "+name[0]+"."
    print(final_result)
except(Exception, psycopg2.DatabaseError) as e:
    print(e)
finally:
    connection.close