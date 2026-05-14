import sqlite3
from datetime import datetime



def connect():

    conn = sqlite3.connect("database/glicemia.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS glucose (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value TEXT,
            data TEXT,
            hour TEXT
        )
    """)

    conn.commit()

    return conn



def add_glucose(value):
    # Conecta ao banco
    conn = sqlite3.connect("database/glicemia.db")
    cursor = conn.cursor()

    # O BANCO gera a data e hora agora
    agora = datetime.now()
    data = agora.strftime("%d/%m/%Y")
    hora = agora.strftime("%H:%M:%S")

    # Insere no banco (certifique-se de que os nomes das colunas batem com seu CREATE TABLE)
    cursor.execute(
        "INSERT INTO glucose (value, data, hour) VALUES (?, ?, ?)",
        (value, data, hora)
    )

    conn.commit()
    conn.close()
    
    # RETORNA os valores para o add.py usar na interface
    return data, hora