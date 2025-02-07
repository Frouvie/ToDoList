import sys
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


def menu() -> None:
    print('Menu:')
    print('1. Select all')
    print('2. Select')
    print('3. Insert')
    print('4. Update')
    print('5. Delete')
    print('6. Exit')


def main():
    try:
        create_table()
    except Exception as error:
        print(f'Error : {error}')
        sys.exit()

    menu()
    
    while True:
        responce = int(input('Choice an action (1-6): '))

        match responce:
            case 1:
                try:
                    tasks = select_all()
                except Exception as error:
                    print(f'Error: {error}')
                    break

                for task in tasks:
                    print(task)
            case 2:
                id = int(input('Enter id: '))
                
                try:
                    task = select(id)
                    print(task)
                except Exception as error:
                    print(f'Error: {error}')
                    break
            case 3:
                title = input("Enter title: ")
                priority = int(input("Enter priority: "))

                try:
                    task = insert(title, priority)
                except Exception as error:
                    print(f'Error: {error}')
                    break
            case 4:
                id = int(input('Enter id: '))
                title = input("Enter title: ")
                priority = int(input("Enter priority: "))

                try:
                    task = update(id, title, priority)
                except Exception as error:
                    print(f'Error: {error}')
                    break
            case 5:
                id = int(input('Enter id: '))

                try:
                    task = delete(id)
                except Exception as error:
                    print(f'Error: {error}')
                    break
            case 6:
                sys.exit()


if __name__ == '__main__':
    main()
