Вася реализовал функцию, которая переводит целое число из десятичной системы в двоичную. 
Но, кажется, она получилась не очень оптимальной.

Попробуйте написать более эффективную программу.

Не используйте встроенные средства языка по переводу чисел в бинарное представление.

Формат ввода
На вход подаётся целое число в диапазоне от 0 до 10000.

Формат вывода
Выведите двоичное представление этого числа.



from typing import List


def body_func(number: int) -> List[str]:
    result = []
    if number == 0:
        result.append('0')
    else:
        while number >= 1:
            if number % 2 == 1:
                result.insert(0, '1')
            else:
                result.insert(0, '0')
            number = number // 2
    return result


def read_input() -> int:
    number = int(input())
    return number


def print_result(result: List[str]) -> None:
    print(''.join(result))


print_result(body_func(read_input()))
