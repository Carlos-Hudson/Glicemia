import sqlite3


def connect():

    conn = sqlite3.connect("database/glicemia.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS glucose (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value TEXT
        )
    """)

    conn.commit()

    return conn


def add_glucose(value):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO glucose (value) VALUES (?)",
        (value,)
    )

    conn.commit()

    conn.close()