import sqlite3

conn = sqlite3.connect('my_db.db')
cursor = conn.cursor()

def create_table() -> None:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks_list (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(128) NOT NULL,
            priority INTEGER NOT NULL
        )
    ''')

    conn.commit()

def insert(title: str, priority: int) -> None:
    cursor.execute('''
        INSERT INTO tasks_list (title, priority) VALUES (?, ?)
    ''', (title, priority))

    conn.commit()

def update(id: int, title: str, priority: int) -> None:
    cursor.execute('''
        UPDATE tasks_list SET
        title = ?, priority = ?
        WHERE id = ?
    ''', (title, priority, id))

    conn.commit()

def delete(id: int) -> None:
    cursor.execute('''
        DELETE FROM tasks_list
        WHERE id = ?
    ''', (id,))

    conn.commit()

def select(id: int):
    cursor.execute('''
        SELECT * FROM tasks_list
        WHERE id = ?
    ''', (id,))

    return cursor.fetchone()


def select_all() -> list:
    cursor.execute('''
        SELECT * FROM tasks_list
        ORDER BY priority DESC
    ''')
    
    return cursor.fetchall()