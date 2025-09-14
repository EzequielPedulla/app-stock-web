from flask import Blueprint, render_template, request, redirect, url_for
from models.products import db, Product


bp = Blueprint('products', __name__)


@bp.route('/')
def index():
    productos = Product.query.all()
    return render_template('index.html', products=productos)


@bp.route('/add', methods=['GET', 'POST'])
def add_product():
    """Agrega un nuevo producto a la base de datos.

    Returns:
        str: Template del formulario o redirección a la lista.
    """
    if request.method == 'POST':
        try:
            # Validar datos del formulario
            name = request.form.get('name', '').strip()
            stock = int(request.form.get('stock', 0))
            price = float(request.form.get('price', 0))
            barcode = request.form.get('barcode', '').strip()

            # Validaciones básicas
            if not name:
                return render_template('add_product.html', error='El nombre es requerido')

            if stock < 0:
                return render_template('add_product.html', error='El stock debe ser mayor o igual a 0')

            if price < 0:
                return render_template('add_product.html', error='El precio debe ser mayor o igual a 0')

            # Crear y guardar producto
            nuevo = Product(name=name, stock=stock,
                            price=price, barcode=barcode)
            db.session.add(nuevo)
            db.session.commit()
            return redirect(url_for('products.index'))

        except ValueError:
            return render_template('add_product.html', error='Datos inválidos. Verifica los números.')
        except Exception as e:
            db.session.rollback()
            return render_template('add_product.html', error=f'Error al guardar: {str(e)}')

    return render_template('add_product.html')


@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    product = Product.query.get_or_404(id)

    if request.method == 'POST':
        try:
            product.name = request.form.get('name', '').strip()
            product.stock = int(request.form.get('stock', 0))
            product.price = float(request.form.get('price', 0))
            product.barcode = request.form.get('barcode', '').strip()

            if not product.name:
                return render_template('edit_product.html', product=product, error='El nombre es requerido')

            if product.stock < 0:
                return render_template('edit_product.html', product=product, error='El stock debe ser mayor o igual a 0')

            if product.price < 0:
                return render_template('edit_product.html', product=product, error='El precio debe ser mayor o igual a 0')

            db.session.commit()
            return redirect(url_for('products.index'))

        except ValueError:
            return render_template('edit_product.html', product=product, error='Datos inválidos. Verifica los números.')
        except Exception as e:
            db.session.rollback()
            return render_template('edit_product.html', product=product, error=f'Error al guardar: {str(e)}')

    return render_template('edit_product.html', product=product)
