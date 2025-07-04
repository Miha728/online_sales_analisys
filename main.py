from product import Product
from product_manager import ProductManager
from cart import Cart
import random

manager = ProductManager()

p1 = Product("Laptop", 3000, 2)
p2 = Product("Telefon", 1500, 3)
p3 = Product("Casti", 300, 5)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

cart = Cart()

selected_products = random.sample(manager.products, 3)
for product in selected_products:
    cart.add_to_cart(product)

cart.display_cart()
print(f"Valoarea totală de plată a coșului: {cart.calculate_total()}")
