import sqlite3

# А4 - бумага
connect = sqlite3.connect('user.db')
# Рука с карандашом
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (20) NOT NULL,
    age INTEGER NOT NULL,
    hobby TEXT
    )
''')
connect.commit()

# CRUD - Create Read Update Delete

def create_user(name, age, hobby):
    # cursor.execute(f"INSERT INTO users(name, age, hobby) VALUES('{name}', {age}, '{hobby}')")

    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES(?, ?, ?)',
        (name, age, hobby)
    )


    connect.commit()
    print("Пользователь добавлен!!")
# create_user("Aidana", 20, "Python")
# create_user("Aizirek", 19,"Спать")
# create_user("Sanira", 18,"Спать")
# create_user("Ardager", 26,"Python")


def read_users():
    cursor.execute('SELECT name, age FROM users')
    users = cursor.fetchall()

       # print(users)
    # for i in users:
    #     print(f"NAME: {i[0]} AGE: {i[1]} ")

def detail_user(id):
    cursor.execute(
        'SELECT * FROM users WHERE id = ?',
        (id,)
    )
    user = cursor.fetchone()
    print(user)
detail_user(1)

# read_users()

def update_user(name, rowid):

    cursor.execute(
        'UPDATE users SET name = ? WHERE rowid = ?',
        (name, rowid)
    )
    connect.commit()
    print(f" Пользователь с id {rowid} обновлен!!!")

# update_user("Martin", 4)

def delete_user(id):
    cursor.execute('DELETE FROM USERS WHERE id = ?', (id,))
    connect.commit()
    print(f" Пользователь с id {id} удален!!! ")

# delete_user(2)

