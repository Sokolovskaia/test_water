import sqlite3



def open_db(url):
    connection = sqlite3.connect(url)
    connection.row_factory = sqlite3.Row
    return connection



def create_table_pets(connection):
    with connection:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_1 (
            test_id INTEGER PRIMARY KEY AUTOINCREMENT
          , name TEXT NOT NULL
        );
        """)
        connection.commit()


def show_all(connection):
    with connection:
        cursor = connection.cursor()
        result = cursor.execute("""
                      SELECT * 
                      FROM test_1""").fetchall()
        return result

