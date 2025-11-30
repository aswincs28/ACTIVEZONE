import psycopg2

try:
    # Establish a connection to the PostgreSQL database
    connection = psycopg2.connect(
        database="turf",               # Replace with your database name
        user="activezone_user",        # Replace with your database username
        password="forgive",       # Replace with your correct password
        host="localhost",              # Host where the database is hosted
        port="5432"                    # Database port
    )
    print("Connection successful")

except Exception as e:
    # Handle any errors that occur during the connection
    print(f"Error: {e}")

finally:
    # Close the connection if it was established
    if 'connection' in locals():  # Check if the variable 'connection' exists
        connection.close()