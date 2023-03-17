class Product:
    def __init__(self, name, price, amount):
        self.__name = name
        self.__price = price
        self.__amount = amount

    def sale(self):
        self.__amount -= 1

    def refund(self):
        self.__amount += 1

    def get_info(self):
        return f"Товар:{self.__name}, цена:{self.__price}, количество:{self.__amount}"


name1 = input()
price1 = float(input())
amount1 = int(input())
method1 = input()

product = Product(name1, price1, amount1)

if method1 == 'sale':
    product.sale()
elif method1 == 'refund':
    product.refund()

print(product.get_info())
