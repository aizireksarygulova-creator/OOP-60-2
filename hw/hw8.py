import sqlite3

def create_table():
    connect = sqlite3.connect('fitness.db')
    cursor = connect.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS workouts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(30) NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sessions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rating INTEGER NOT NULL,
        date VARCHAR(30) NOT NULL,
        workout_id INTEGER NOT NULL,
        FOREIGN KEY(workout_id) REFERENCES workouts(id)
    )
    ''')

    connect.commit()
    connect.close()

# create_table()

print("Таблицы созданы!")

import sqlite3

def insert_data():
    connect = sqlite3.connect('fitness.db')
    cursor = connect.cursor()


    cursor.executemany(
        'INSERT INTO workouts (name) VALUES (?)',
        [
            ("Планка",),
            ("Приседания",),
            ("Отжимания",)
        ]
    )

    cursor.executemany(
        'INSERT INTO sessions (rating, date, workout_id) VALUES (?,?,?)',
        [
            (4, "2025-11-20", 1),
            (5, "2025-11-21", 2),
            (3, "2025-11-22", 3)
        ]
    )

    connect.commit()
    connect.close()
    print("Данные добавлены!")

# insert_data()

import sqlite3

def show_data():
    connect = sqlite3.connect('fitness.db')
    cursor = connect.cursor()

    print("Таблица workouts:")
    cursor.execute("SELECT * FROM workouts")
    print(cursor.fetchall())

    print("\nТаблица sessions:")
    cursor.execute("SELECT * FROM sessions")
    print(cursor.fetchall())

    connect.close()

# show_data()

def get_all_sessions():
    connect = sqlite3.connect('fitness.db')
    cursor = connect.cursor()

    cursor.execute('''
    SELECT workouts.name, sessions.date, sessions.rating
    FROM workouts INNER JOIN sessions 
    ON workouts.id = sessions.workout_id
    ''')

    users = cursor.fetchall()
    print(users)

    connect.close()

def get_best_session():
    connect = sqlite3.connect('fitness.db')
    cursor = connect.cursor()

    cursor.execute(
        '''
        SELECT workouts.name, MAX(sessions.rating) 
        FROM workouts INNER JOIN sessions 
        ON workouts.id = sessions.workout_id
        '''
    )

    users = cursor.fetchall()
    print(users)

    connect.close()

def get_hard_workouts():
    connect = sqlite3.connect('fitness.db')
    cursor = connect.cursor()

    cursor.execute(
        '''
        SELECT name FROM workouts WHERE id IN (
            SELECT workout_id FROM sessions
            WHERE rating >= 70
        )
        '''
    )

    users = cursor.fetchall()
    print(users)

    connect.close()

def create_my_view():
    connect = sqlite3.connect('fitness.db')
    cursor = connect.cursor()

    cursor.execute('''
        CREATE VIEW IF NOT EXISTS my_view AS
        SELECT workouts.name, sessions.rating, sessions.date
        FROM workouts LEFT JOIN sessions 
        ON workouts.id = sessions.workout_id
    ''')

    connect.commit()
    connect.close()

def get_view():
    connect = sqlite3.connect('fitness.db')
    cursor = connect.cursor()

    cursor.execute('SELECT * FROM my_view')
    users = cursor.fetchall()
    print(users)

    connect.close()
