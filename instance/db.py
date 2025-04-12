import sqlite3

DATABASE_NAME = "./instance/notes.db"


def get_db_connection():
    """This function returns the connection to the database."""
    conn = sqlite3.connect(DATABASE_NAME)
    # INFO This line returns data as dictionary
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    query = """CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT,
    selected BOOLEAN NOT NULL DEFAULT 0)"""
    with get_db_connection() as conn:
        conn.execute(query)
