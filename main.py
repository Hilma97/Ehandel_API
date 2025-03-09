from fastapi import FastAPI
import sqlite3

app = FastAPI()

# Skapa en enkel databas
conn = sqlite3.connect("products.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price REAL, stock INTEGER)''')
conn.commit()

@app.get("/")
def read_root():
    return {"message": "Välkommen till E-handels-API"}

@app.get("/products")
def get_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    return {"products": products}

@app.post("/products")
def add_product(name: str, price: float, stock: int):
    cursor.execute("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", (name, price, stock))
    conn.commit()
    return {"message": "Produkt tillagd"}
