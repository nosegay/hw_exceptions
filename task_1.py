import errno


class Error(Exception):
    pass


if __name__ == '__main__':
    try:
        input_formula = input('Введите выражение для подсчета: ')
        if len(input_formula.split()) != 3:
            raise Error('Введено неверное количество аргументов!')
    except Error as e:
        print(e)
        exit(errno.EINVAL)

    sign, num_1, num_2 = input_formula.split()

    assert sign in ('+', '-', '*', '/'), 'Операции не найдено!'

    try:
        num_1 = int(num_1)
        num_2 = int(num_2)
    except ValueError as e:
        print('Неверный формат входных данных: работа со строками недопустима!')
        exit(errno.EPERM)

    assert (num_1 * num_2 >= 0), 'Работа с отрицательными числами не предусмотрена!'

    try:
        if sign == '+':
            print(f'Результат: {num_1 + num_2}')
        elif sign == '*':
            print(f'Результат: {num_1 * num_2}')
        elif sign == '-':
            print(f'Результат: {num_1 - num_2}')
        elif sign == '/':
            print(f'Результат: {num_1 / num_2}')
    except ZeroDivisionError as e:
        print(e)
        exit(errno.EINVAL)
    except Exception as e:
        print(e)
