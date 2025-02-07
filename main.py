import sys
import db


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
        db.create_table()
    except Exception as error:
        print(f'Error : {error}')
        sys.exit()

    menu()
    
    while True:
        responce = int(input('Choice an action (1-6): '))

        match responce:
            case 1:
                try:
                    tasks = db.select_all()
                except Exception as error:
                    print(f'Error: {error}')
                    break

                for task in tasks:
                    print(task)
            case 2:
                id = int(input('Enter id: '))
                
                try:
                    task = db.select(id)
                    print(task)
                except Exception as error:
                    print(f'Error: {error}')
                    break
            case 3:
                title = input("Enter title: ")
                priority = int(input("Enter priority: "))

                try:
                    task = db.insert(title, priority)
                except Exception as error:
                    print(f'Error: {error}')
                    break
            case 4:
                id = int(input('Enter id: '))
                title = input("Enter title: ")
                priority = int(input("Enter priority: "))

                try:
                    task = db.update(id, title, priority)
                except Exception as error:
                    print(f'Error: {error}')
                    break
            case 5:
                id = int(input('Enter id: '))

                try:
                    task = db.delete(id)
                except Exception as error:
                    print(f'Error: {error}')
                    break
            case 6:
                sys.exit()


if __name__ == '__main__':
    main()
