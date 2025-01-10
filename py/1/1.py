n = int(input("Введите число: "))
for i in range(1, n + 1):
    print(i)

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
if num1 > num2:
    print(f"Большее число: {num1}")
elif num2 > num1:
    print(f"Большее число: {num2}")
else:
    print("Числа равны")