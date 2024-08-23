import sqlite3

FILE_DB = 'database/bot_DB.db'


def initiate_db():
    connection_ = sqlite3.connect(FILE_DB)
    cursor_ = connection_.cursor()

    cursor_.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')

    connection_.commit()
    connection_.close()


def is_included(username):
    connection_ = sqlite3.connect(FILE_DB)
    cursor_ = connection_.cursor()

    cursor_.execute(f"SELECT Count(*) FROM Users WHERE username = '{username}'")
    result = bool(cursor_.fetchone()[0])

    connection_.commit()
    connection_.close()

    return result


def add_user(username, email, age):
    connection_ = sqlite3.connect(FILE_DB)
    cursor_ = connection_.cursor()

    cursor_.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)",
                    (username, email, age, 1000))

    connection_.commit()
    connection_.close()


if __name__ == "__main__":
    initiate_db()

    # connection = sqlite3.connect(FILE_DB)
    # cursor = connection.cursor()
    #
    # cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)",
    #                ("pvt_Pyle1", "test1@gmail.com", 40, 1000))
    # cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)",
    #                ("pvt_Pyle2", "test2@gmail.com", 39, 1000))
    # cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)",
    #                ("pvt_Pyle3", "test3@gmail.com", 25, 1000))
    # cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)",
    #                ("pvt_Pyle4", "test4@gmail.com", 52, 1000))
    #
    # connection.commit()
    # connection.close()
