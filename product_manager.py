from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        for product in self.products:
            product.display_info()

    def calculate_total_value(self):
        total = sum(product.price * product.quantity for product in self.products)
        print(f"Valoarea totală a inventarului: {total}")

    def remove_product_by_name(self, name):
        self.products = [product for product in self.products if product.name != name]
