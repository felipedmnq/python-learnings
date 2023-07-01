import sqlite3
from sqlite3 import Error


def create_connection(db_file: str) -> None:
    """create a database connection to a SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def create_sqlite_table(db_name: str, sql_script: str) -> None:
    """create a table in a SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        print(sqlite3.version)

        with open(sql_script, "r") as file:
            sql_script = file.read()

        c.execute(sql_script)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    db_file_name = "pythonsqlite.db"
    sql_script = "db_init/create_table.sql"
    create_sqlite_table(db_file_name, sql_script)
