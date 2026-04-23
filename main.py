# 3. Phone
class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_price(self):
        print(f"{self.brand} narxi {self.price}$")


p = Phone("iPhone", 1200)
p.show_price()


# 4. Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def about(self):
        print(f"Kitob: {self.title}, Muallif: {self.author}")


b = Book("Python", "Aliyev")
b.about()
