import sqlite3

con = sqlite3.connect('test.db')
cursor = con.cursor()

cursor.execute('''TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL)'''
)

cursor.execute('''CREATE TABLE customers ( customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
 first_name TEXT NOT NULL,
 last_name TEXT NOT NULL,
 email TEXT NOT NULL UNIQUE );''')

cursor.execute('''CREATE TABLE orders ( order_id INTEGER PRIMARY KEY AUTOINCREMENT,
 customer_id INTEGER NOT NULL, product_id INTEGER NOT NULL,
  quantity INTEGER NOT NULL, order_date DATE NOT NULL,
   FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
 FOREIGN KEY (product_id) REFERENCES products(product_id) );''')

choose = input('Enter your choice: ')
if choose == '1':
    product_name = input('Enter product name: ')
    product_category = input('Enter product category: ')
    product_price = input(int('Enter product price: '))
    cursor.execute('''INSERT INTO products (product_name, product_category, product_price) VALUES (?, ?, ?)''', (product_name, product_category, product_price))
    con.commit()