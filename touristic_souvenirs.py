
from tabulate import tabulate
product_list = []

class Product:
    count_code = 0

    def __init__(self, name, category, price):
        Product.count_code += 1
        self.code = Product.count_code
        self.name = name
        self.category = category
        self.price = price
        product_list.append(self)

    def __repr__(self):
        return f"{self.code}, {self.name}, {self.category}, ${self.price}"

    def search_by_name(self, name):
        ...
    
    def get_total_price(product_list, total_price = 0):
        if len(product_list) == 0:
            return total_price
        
        product = product_list[0]

        total_price += product.price 
        return total_price + Product.get_total_price(product_list[1:])
    


#-------------------------------------------------------------------------

p1 = Product("sombrero", "vestimenta", 15000)
p2 = Product("llavero", "miscelaneo", 2000)

print(tabulate(
    [(p.code, p.name, p.category, p.price) for p in product_list],
    headers=["Código", "Nombre", "Categoría", "Precio"],
    tablefmt="fancy_grid"
))

print (
f"costo total: ${Product.get_total_price(product_list)}")