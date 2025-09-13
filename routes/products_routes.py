from flask import Blueprint, render_template, request, redirect, url_for
from models.products import db, Product


bp = Blueprint('products', __name__)


@bp.route('/')
def index():
    productos = Product.query.all()
    return render_template('index.html', products=productos)


@bp.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        precio = request.form['precio']

        nuevo = Product(nombre=nombre, cantidad=cantidad, precio=precio)
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('products.index'))

    return render_template('add_product.html')
