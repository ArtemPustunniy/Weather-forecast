import sqlite3

db_name = 'weather.sqlite'

conn = None
cursor = None


def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()


def close():
    cursor.close()
    conn.close()


def do(query):
    cursor.execute(query)
    conn.commit()


def create():
    open()
    cursor.execute('PRAGMA foreign_key=on')
    do('''CREATE TABLE IF NOT EXISTS weather_by_coords(
                                                id INTEGER PRIMARY KEY,
                                                city_name VARCHAR,
                                                latitude VARCHAR,
                                                longitude VARCHAR,
                                                date_of_request VARCHAR,
                                                temperature VARCHAR,
                                                temperature_feels VARCHAR,
                                                pressure VARCHAR)''')

    close()


create()
