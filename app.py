from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


def get_products():
    """Obtiene todos los productos de la base de datos.

    Returns:
        list: Lista de tuplas con los datos de los productos.
    """
    conn = sqlite3.connect('database/inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id,barcode,name,price,stock FROM products')
    products = cursor.fetchall()
    conn.close()
    return products


@app.route('/')
def index():
    """Página principal que muestra la lista de productos.

    Returns:
        str: HTML renderizado con la lista de productos.
    """
    return render_template('index.html', products=get_products())


if __name__ == '__main__':
    app.run(debug=True)
