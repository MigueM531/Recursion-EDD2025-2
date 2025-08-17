from tabulate import tabulate

class Product:
    count_code = 0

    def __init__(self, name, category, price):
        Product.count_code += 1
        self.code = Product.count_code
        self.name = name
        self.category = category
        self.price = price

    def __repr__(self):
        data = [[self.code, self.name, self.category, self.price]]
        return tabulate(data, headers=["Código", "Nombre", "Categoría", "Precio"],
         tablefmt="fancy_grid")

    def search_by_name(list, target, first = 0, end = None):
        if end is None:
            end = len(list) - 1
        
        if first > end:
            return "NO SE ENCOTRÓ EL PRODUCTO"
        
        mid = (first + end) // 2
        if list[mid].name == target:
            return list[mid]
        elif list[mid].name > target:
            return Product.search_by_name(list, target, first, mid -1)
        else:
            return Product.search_by_name(list, target, mid + 1, end)
        
    
    def get_total_price(list, total_price = 0):
        if len(list) == 0:
            return total_price
        
        product = list[0]

        total_price += product.price 
        return total_price + Product.get_total_price(list[1:])
    


#-------------------------------------------------------------------------

product_list = [
    Product("camiseta", "Ropa", 35000),
    Product("escarapela", "Accesorios", 5000),
    Product("imán", "Decoración", 8000),
    Product("llavero", "Accesorios", 7000),
    Product("mug", "Hogar", 20000),
    Product("póster", "Decoración", 12000),
    Product("pulsera", "Accesorios", 10000),
    Product("ruana", "Ropa", 60000),
    Product("sombrero", "Ropa", 15000),
    Product("vaso térmico", "Hogar", 25000)
]

print("LISTA DE ARTICULOS")
print(tabulate(
    [(p.code, p.name, p.category, p.price) for p in product_list],
    headers=["Código", "Nombre", "Categoría", "Precio"],
    tablefmt="fancy_grid"
))


print(Product.search_by_name(product_list, "waos"))

print (
f"costo total: ${Product.get_total_price(product_list)}")