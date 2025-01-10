def read_file(filename, mode='all'):
    try:
        with open(filename, 'r') as file:
            if mode == 'all':
                content = file.read()
                print("Содержимое файла:")
                print(content)
            elif mode == 'line_by_line':
                print("Построчное чтение:")
                for line in file:
                    print(line.strip())
            else:
                print("Неправильный режим чтения")
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")


with open('example.txt', 'w') as file:
    file.write("Первая строка\nВторая строка\nТретья строка")


read_file('example.txt', mode='all')
read_file('example.txt', mode='line_by_line')

def write_to_file(filename):
    user_input = input("Введите текст для записи в файл: ")
    with open(filename, 'w') as file:
        file.write(user_input)
    print(f"Текст записан в файл {filename}")

def append_to_file(filename):
    user_input = input("Введите текст для добавления в файл: ")
    with open(filename, 'a') as file:
        file.write(user_input)
    print(f"Текст добавлен в файл {filename}")


write_to_file('user_input.txt')


append_to_file('user_input.txt')

def safe_read_file(filename, mode='all'):
    try:
        with open(filename, 'r') as file:
            if mode == 'all':
                content = file.read()
                print("Содержимое файла:")
                print(content)
            elif mode == 'line_by_line':
                print("Построчное чтение:")
                for line in file:
                    print(line.strip())
            else:
                print("Неправильный режим чтения")
    except FileNotFoundError:
        print(f"Файл {filename} не найден. Пожалуйста, убедитесь, что файл существует.")

safe_read_file('non_existing_file.txt')