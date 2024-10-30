import conn as cn
from psycopg2 import sql


def read_table():
    try:
        connection = cn.conn
        cursor = connection.cursor()
        read_query = sql.SQL("SELECT * FROM alumnes")
        cursor.execute(read_query)

        # commit
        connection.commit()
    except Exception as e:
        print(f"Error updating records: {e}")
    finally:
        cursor.close()

