import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database", "inventory.db")
SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_PATH}"
