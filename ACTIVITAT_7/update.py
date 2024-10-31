# Arxiu que conté una funció que modifica algun camp o tots
import conn as cn
from psycopg2 import sql


def update_table(idAlumne, nomAlumne):  # functions with camps to be updated
    try:
        connection = cn.conn
        cursor = connection.cursor()

        # Define the SQL query and parameters for updating
        update_query = sql.SQL("UPDATE alumnes SET nomAlumne = %s WHERE idAlumne = %s")
        cursor.execute(update_query, (nomAlumne, idAlumne))

        # Commit the changes
        connection.commit()
        print("Record updated successfully.")

    except Exception as e:  # exception in case of an error
        print(f"Error updating records: {e}")
    finally:
        cursor.close()

