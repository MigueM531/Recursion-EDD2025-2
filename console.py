from tabulate import tabulate
from touristic_souvenirs import Product, product_list

def menu():

    print("|--------TIENDA DE SOUVENIRS--------|")
    print("-------------------------------------")
    print("Elija una de las siguientes opciones:")
    print("|0| - Mostrar artículos")
    print("|1| - Buscar articulo por nombre")
    print("|2| - Calcular precio total")
    print("|3| - Consultar precio promedio por categoria del producto")
    print("|4| - Ordenar por precio")
    print("|5| - Buscar por rango de precio")
    print("|6| - Recomendaciones de compra")
    print("|#| - Terminar")

    while True:
        option = input("Marque su opción a elegir ---> ")

        if option == "0":
            print("LISTA DE ARTICULOS")
            print(tabulate(
            [(p.code, p.name, p.category, p.price) for p in product_list],
            headers=["Código", "Nombre", "Categoría", "Precio"],
            tablefmt="fancy_grid"
            ))

        elif option == "1":
            name = input("Escriba el nombre del artículo: ")
            print(Product.search_by_name(product_list, name))

        elif option == "2":
            print (f"costo total: ${Product.get_total_price(product_list)}")

        elif option == "3":
            category = input("Buscar por la categoría: ")
            print(f"Precio promedio ${Product.category_average_price(product_list, category)}")


        elif option == "5":
            min = int(input("Ingrese le precio mínimo: "))
            max = int(input("Ingrese el precio máximo: "))
            products = Product.search_price_range(product_list, min, max)
            print(f"BUSQUEDA EN RANGO: {min} - {max}")
            print(tabulate([(p.code, p.name, p.category, p.price) for p in products],
                   headers=["Código", "Nombre", "Categoría", "Precio"],
                    tablefmt="fancy_grid"))
            
        elif option == "6":
            print("PRODUCTOS RECOMENDADOS:")
            product = input("Buscar similares a: ")
            products = Product.recommend_product(product_list, product)
            print(tabulate([(p.code, p.name, p.category, p.price) for p in products],
               headers=["Código", "Nombre", "Categoría", "Precio"],
                tablefmt="fancy_grid"))

        elif option == "#":
            print("            CHAU")
            break

menu()