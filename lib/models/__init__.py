import sqlite3

CONN = sqlite3.connect('classroom.db')
CURSOR = CONN.cursor()
CURSOR.execute('PRAGMA foreign_keys = ON;')

