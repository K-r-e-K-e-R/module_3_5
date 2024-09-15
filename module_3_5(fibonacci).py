

def get_multiplied_digits(number):
    # Преобразование числа в строку
    str_number = str(number)

    # Условия выхода из рекурсии
    if len(str_number) == 0:  # Если строка пустая
        return 1  # Возврат числа 1
    elif len(str_number) == 1:  # Если осталась только одна цифра
        return int(str_number)  # Вернуть эту цифру как целое число

    # Извлечение первой цифры и преобразование её в целое число
    first = int(str_number[0])

    # Рекурсивный метод
    return first * get_multiplied_digits(int(str_number[1:]))


if __name__ == "__main__":
    number = int(input("Введите число для умножения цифр: "))
    result = get_multiplied_digits(number)
    print("Результат умножения:", result)
