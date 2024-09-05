import sqlite3

ENABLE_FOREIGN_KEY = "PRAGMA foreign_keys = ON;"


def init_db():
    with sqlite3.Connection("database.db") as conn:
        cursor = conn.cursor()
        cursor.executescript(ENABLE_FOREIGN_KEY)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL)
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                content TEXT NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users(id))
         """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                post_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                content TEXT NOT NULL,
                FOREIGN KEY(post_id) REFERENCES posts(id),
                FOREIGN KEY(user_id) REFERENCES users(id))
        """)
        conn.commit()

