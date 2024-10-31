# Arxiu que conté una funció que elimina un registre de la taula
import conn as cn
from psycopg2 import sql


def delete_data(idAlumne):
    try:
        connection = cn.conn
        cursor = connection.cursor()
        # query to delete data from the table
        delete_query = sql.SQL("DELETE FROM alumnes WHERE idAlumne = %s")
        cursor.execute(delete_query, (idAlumne, ))  # To execute the query

        # commit
        connection.commit()
        print("Deleted successfully")
    except Exception as e:
        print(f"Error deleting data{e}")
    finally:
        cursor.close()
