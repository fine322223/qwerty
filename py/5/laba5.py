class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"

odin = Book("Дежавю", "Кизару", 2022)
print(odin.get_info())

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius

circle = Circle(5)
print(f"Исходный радиус: {circle.get_radius()}")
circle.set_radius(10)
print(f"Новый радиус: {circle.get_radius()}")