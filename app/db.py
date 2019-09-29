import sqlite3



def open_db(url):
    connection = sqlite3.connect(url)
    connection.row_factory = sqlite3.Row
    return connection



# def create_table_test_1(connection):
#     with connection:
#         cursor = connection.cursor()
#         cursor.execute("""
#         CREATE TABLE IF NOT EXISTS test_1 (
#             test_id INTEGER PRIMARY KEY AUTOINCREMENT
#           , name TEXT NOT NULL
#         );
#         """)
#         connection.commit()

def create_table_source_data(connection):
    with connection:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS source_data (
            water_id INTEGER PRIMARY KEY AUTOINCREMENT
          , id_csv TEXT NOT NULL
          , name_csv TEXT NOT NULL
          , id_object INTEGER NOT NULL
          , object TEXT NOT NULL
          , type_object TEXT NOT NULL
          , prev_object_id TEXT
          , next_object_id TEXT
          , accidents INTEGER
          , amortization_wear INTEGER
          , actual_parameters INTEGER
          , unit TEXT
        );
        """)
        connection.commit()


def create_table_visual_data(connection):
    with connection:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS visual_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT
          , id_object INTEGER NOT NULL
          , id_csv TEXT NOT NULL
          , name_object TEXT NOT NULL
          , object TEXT NOT NULL
          , type_object TEXT NOT NULL
          , prev_object_id TEXT
          , next_object_id TEXT
          , accidents INTEGER
          , accidents__sum INTEGER
          , amortization_wear_average INTEGER
          , actual_parameters_sum INTEGER
          , unit TEXT
          , number_of_objects INTEGER
        );
        """)
        connection.commit()


def show_all(connection):
    with connection:
        cursor = connection.cursor()
        result = cursor.execute(""" SELECT id_csv
      , object
      , id_object
      , COUNT(id_object) count
      , AVG(amortization_wear) avg
      , SUM(actual_parameters) sum
 FROM source_data
GROUP BY prev_object_id, next_object_id""").fetchall()
        return result

