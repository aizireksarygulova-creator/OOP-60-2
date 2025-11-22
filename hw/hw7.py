import sqlite3

connect = sqlite3.connect("store.db")
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(20) NOT NULL,
        price INTEGER NOT NULL,
        category TEXT,
        in_stock INTEGER
    )
''')
connect.commit()


def create_products(name, price, category, in_stock):
    cursor.execute(
        "INSERT INTO products (name, price, category, in_stock) VALUES (?, ?, ?, ?)",
        (name, price, category, in_stock)
    )
    connect.commit()
    print(f"Товар добавлен!")


# create_products("Шоколад", 55.5, "Еда", 120)
# create_products("Наушники", 950.0, "Электроника", 15)
# create_products("Тетрадь", 25.0, "Канцелярия", 200)


def read_products():
    cursor.execute('SELECT * FROM products')
    return cursor.fetchall()

def update_products(products_id, new_price):
    cursor.execute(
        'UPDATE products SET price = ? WHERE id = ?',
        (new_price, products_id)
    )
    connect.commit()
    print(f"Продукт с id {products_id} обновлен!!!")

# update_products("1", 65)

def delete_product(product_id):
    cursor.execute(
     'DELETE FROM products WHERE id = ?',
     (product_id,))
    connect.commit()
print(f" Продукт с id {id} удален!!! ")

# delete_product(2)

connect.close()




