# To create records for the table

from psycopg2 import sql
import conn  # Import connection details


def insert_records(idAlumne, nomAlumne, curs, cicle, grup, aula):
    try:
        # Use the connection from conn module
        connection = conn.conn  # Make sure this is the established connection from conn.py
        cursor = connection.cursor()

        # SQL command to insert a new record
        insert_query = sql.SQL("INSERT INTO alumnes(idAlumne, nomAlumne, curs, cicle, grup, aula) VALUES (%s, %s, %s, %s, %s, %s)")

        # Execute the insert command
        cursor.execute(insert_query, (idAlumne, nomAlumne, curs, cicle, grup, aula))

        # Commit the changes
        connection.commit()

    except Exception as e:
        print(f"Error creating records: {e}")  # Print the exception for better debugging
    finally:
        cursor.close()  # close the cursor
