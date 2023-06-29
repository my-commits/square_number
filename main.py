from two_number_adder_my_commits.add_numbers import add_two_numbers


def square_number(num):
    square = num ** 2
    return square


if __name__ == '__main__':
    num1 = int(input('Первое число: '))
    num2 = int(input('Второе число: '))
    print('Сумма', add_two_numbers(num1, num2))
    input_number = int(input("Введите число: "))
    result = square_number(input_number)
    print("Квадрат числа", input_number, "Равен", result)
