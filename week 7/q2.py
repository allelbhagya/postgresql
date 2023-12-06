import sys
import os
import psycopg2

try:
   connection = psycopg2.connect(
       database = sys.argv[1],
       user = os.environ.get('PGUSER'),
       password = os.environ.get('PGPASSWORD'),
       host = os.environ.get('PGHOST'),
       port = os.environ.get('PGPORT'))
       
   cursor = connection.cursor()
   query = "select team_id from teams where jersey_home_color <> jersey_away_color"
   
   cursor.execute(query)
   alpha = {'A': 8, 'B': 9, 'C': 10, 'D': 11, 'E': 12, 'F': 13, 'G': 14, 'H': 15, 'I': 16, 'J': 17, 'K': 18, 'L': 19, 'M': 20, 'N': 21, 'O': 22, 'P': 23, 'Q': 24, 'R': 25, 'S': 0, 'T': 1, 'U': 2, 'V': 3, 'W': 4, 'X': 5, 'Y': 6, 'Z': 7}
   nums = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}

   result = cursor.fetchall()

   for res in result:
       print(res[0])
       z = []
       for i in res[0]:
           if i.isalpha():
               c = (nums[alpha[i]])
               z.append(str(c))
           else:
                xyz = (int(i) + 7) % 10
                z.append(str(xyz))
       print(''.join([str(elem) for elem in z]))

   cursor.close()
except(Exception, psycopg2.DatabaseError) as error:
   print(error)
finally:
   connection.close