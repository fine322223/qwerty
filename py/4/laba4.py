import math
n = int(input('Введите число: '))
r = math.sqrt(n)
print(f"Квадратный корень {n} равен {r}")

from datetime import datetime
dt = datetime.now()
print(f"Дата и время: {dt}")

import my_module
a = int(input('Введите число: '))
b = int(input('Введите число: '))
res = my_module.summa(a, b)
print(f"Сумма: {res}")

from mods import mod1, mod2
rm = mod1.mult(4, 5)
rd = mod2.div(20, 4)
print(f"Произведение: {rm}")
print(f"Результат деления: {rd}")