import sqlite3

FILE_DB = 'database/bot_DB.db'


def initiate_db(file_path=FILE_DB):
    connection_ = sqlite3.connect(file_path)
    cursor_ = connection_.cursor()

    cursor_.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

    connection_.commit()
    connection_.close()


def get_all_products(file_path=FILE_DB):
    connection_ = sqlite3.connect(file_path)
    cursor_ = connection_.cursor()

    cursor_.execute("SELECT title, description, price from Products")
    result = cursor_.fetchall()

    connection_.commit()
    connection_.close()

    return result


if __name__ == "__main__":
    initiate_db('bot_DB.db')

    connection = sqlite3.connect('bot_DB.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Products(title, description, price) VALUES(?, ?, ?)",
                   ('Зеленоцвет', 'Снимает усталость', 200))
    cursor.execute("INSERT INTO Products(title, description, price) VALUES(?, ?, ?)",
                   ('Цветущий зеленоцвет', 'Лечит переутомление', 500))
    cursor.execute("INSERT INTO Products(title, description, price) VALUES(?, ?, ?)",
                   ('Пурпурный мох', 'Лечит отравление', 1000))
    cursor.execute("INSERT INTO Products(title, description, price) VALUES(?, ?, ?)",
                   ('Цветущий пурпурный мох', 'Выводит яды и токсины', 2000))

    connection.commit()
    connection.close()

    product_list = get_all_products('bot_DB.db')
    print(product_list)
