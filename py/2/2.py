def greet(name):
    print(f"Привет, {name}!")

def square(number):
    return number ** 2

def max_of_two(x, y):
    return x if x > y else y

def describe_person(name, age=30):
    print(f"Имя: {name}, Возраст: {age}")

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True