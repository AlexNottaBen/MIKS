from app import app, database
from Product import Product
from ProductPhoto import ProductPhoto


app.app_context().push()
database.create_all()
