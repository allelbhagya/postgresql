import psycopg2

# Replace these with your actual database credentials
dbname = 'practice'
user = 'postgres'
password = '5april2002'
host = '127.0.0.1'  # e.g., 'localhost' or '127.0.0.1'
port = '5432'  # e.g., '5432'
table_name = 'student'

# Establish a connection to the PostgreSQL database
try:
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("Connected to the database")

    # Create a cursor to interact with the database
    with connection.cursor() as cursor:
        # Example query: select all rows from a specific table
        query = f"SELECT * FROM {table_name};"
        cursor.execute(query)

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Print the column names
        col_names = [desc[0] for desc in cursor.description]
        print("\t".join(col_names))

        # Print the data
        for row in rows:
            print("\t".join(str(cell) for cell in row))

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the connection when done
    if connection:
        connection.close()
        print("Connection closed")