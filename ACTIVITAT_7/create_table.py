# To create table
import conn as cn  # For the connection setup


def create_table():
    try:
        # Connect using the existing connection in conn.py
        connection = cn.conn
        cursor = connection.cursor()

        # Create table query
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS alumnes(
            idAlumne SERIAL PRIMARY KEY,
            nomAlumne VARCHAR(20),
            curs VARCHAR(20),
            cicle varchar(20),
            grup varchar(10),
            aula varchar(10)
        );
        '''

        # Execute and commit the table creation
        cursor.execute(create_table_query)
        connection.commit()
        print("Table 'alumnes' created successfully or already exists.")

    except Exception as e:
        print(f"Error creating table: {e}")

    finally:
        cursor.close()
