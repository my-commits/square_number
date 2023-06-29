def square_number(num):
    square = num ** 2
    return square


if __name__ == '__main__':
    input_number = int(input("Введите число: "))
    result = square_number(input_number)
    print("Квадрат числа", input_number, "Равен", result)
