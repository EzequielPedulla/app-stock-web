from flask import Flask, redirect, url_for
from routes.products_routes import bp as products_bp
from models.products import db
from config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)

# Configurar la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db.init_app(app)

# Registrar el blueprint de productos
app.register_blueprint(products_bp, url_prefix='/products')

# Crear las tablas de la base de datos
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    """Página principal que redirige a la lista de productos.

    Returns:
        Response: Redirección a la página de productos.
    """
    return redirect(url_for('products.index'))


if __name__ == '__main__':
    app.run(debug=True)
