from product import Product
from product_manager import ProductManager

manager = ProductManager()

p1 = Product("Laptop", 3000, 2)
p2 = Product("Telefon", 1500, 3)
p3 = Product("Casti", 300, 5)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

manager.display_products()
manager.calculate_total_value()
