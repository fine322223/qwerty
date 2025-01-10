import hashlib
class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password_hash = self.__hash_password(password)

    def __hash_password(self, password):

        return hashlib.sha256(password.encode()).hexdigest()

    def set_password(self, new_password):

        self.__password_hash = self.__hash_password(new_password)

    def check_password(self, password):

        return self.__hash_password(password) == self.__password_hash

user = UserAccount("username123", "user@example.com", "123")

print(user.check_password("321"))
print(user.check_password("123"))

user.set_password("1234")

print(user.check_password("123"))
print(user.check_password("1234"))

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Тип топлива: {self.fuel_type}"

vehicle = Vehicle("VAZ", "2113")
car = Car("Belaz", "75710", "Дизель")

print(vehicle.get_info())
print(car.get_info())