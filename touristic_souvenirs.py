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

    def search_by_name(product_list, target, first = 0, end = None):
        if end is None:
            end = len(product_list) - 1
        
        if first > end:
            return "NO SE ENCOTRÓ EL PRODUCTO"
        
        mid = (first + end) // 2
        if product_list[mid].name == target:
            return product_list[mid]
        elif product_list[mid].name > target:
            return Product.search_by_name(product_list, target, first, mid -1)
        else:
            return Product.search_by_name(product_list, target, mid + 1, end)
        
    
    def get_total_price(product_list, total_price = 0):
        if len(product_list) == 0:
            return total_price
        
        product = product_list[0]

        total_price += product.price 
        return total_price + Product.get_total_price(product_list[1:])
    

    def category_average_price(product_list, category, count = 0, total_price = 0):
        if len(product_list) == 0:
            if count == 0:
                return "CATEGORIA NO EXISTENTE"
            return round(total_price / count)
        
        product = product_list[0]

        if product.category != category:
            return Product.category_average_price(product_list[1:], category, count, total_price)

        else:
            total_price += product.price
            count += 1
            return Product.category_average_price(product_list[1:], category, count, total_price)
        
    def sort_price():
        pass

    def search_price_range(product_list, mini, maxi, aux_list = []):
        if len(product_list) == 0:
            if len(aux_list) == 0:
                return f"No hay productos entre el rango de precio"
            return aux_list
        
        if product_list[0].price >= mini and product_list[0].price <= maxi:
            aux_list.append(product_list[0])
        return Product.search_price_range(product_list[1:], mini, maxi, aux_list) 


    def recommend_product(product_list, target, idx = 0, category = ""):
        if idx == len(product_list):
            return []
        current = product_list[idx]

        if current.category == target.category and current != target:
            return [current] + Product.recommend_product(product_list, target, idx + 1, category)
        else:
            return Product.recommend_product(product_list, target, idx + 1, category)

#-------------------------------------------------------------------------

product_list = [
    Product("camiseta", "Ropa", 35000),
    Product("escarapela", "Accesorios", 5000),
    Product("iman", "Decoración", 8000),
    Product("llavero", "Accesorios", 7000),
    Product("mug", "Hogar", 20000),
    Product("poster", "Decoración", 12000),
    Product("pulsera", "Accesorios", 10000),
    Product("ruana", "Ropa", 60000),
    Product("sombrero", "Ropa", 15000),
    Product("vaso termico", "Hogar", 25000)
]
