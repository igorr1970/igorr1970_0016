class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            return ''  # Если файла нет, возвращаем пустую строку

    def add(self, *products):
        existing_products = self.get_products().splitlines()
        existing_names = {product.split(', ')[0] for product in existing_products}

        for product in products:
            if product.name in existing_names:
                print(f'Продукт {product} уже есть в магазине')
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + '\n')
    # Создаем экземпляры класса Shop и Product


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

# Печатаем строковое представление продукта p2
print(p2)  # Вывод: Spaghetti, 3.4, Groceries

# Добавляем продукты в магазин
s1.add(p1, p2, p3)

# Получаем и печатаем все продукты из магазина
print(s1.get_products())