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

    query ="select students.student_fname, departments.department_name, students.dob from students,departments where students.student_fname = '{}' and departments.department_code = students.department_code".format(name)
    cursor.execute(query)
    result = cursor.fetchall()
    for res in result:
        if res[2].year %2 == 0:
            print(res[0]+','+res[1]+','+"Even")
        else:
            print(res[0]+','+res[1]+','+"Odd")
except(Exception, psycopg2.DatabaseError) as e:
    print(e)
finally:
    connection.close