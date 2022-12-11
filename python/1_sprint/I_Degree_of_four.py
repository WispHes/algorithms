Напишите программу, которая определяет, будет ли положительное целое число степенью четвёрки.

Подсказка: степенью четвёрки будут все числа вида 4n, где n – целое неотрицательное число.

Формат ввода
На вход подаётся целое число в диапазоне от 1 до 10000.

Формат вывода
Выведите «True», если число является степенью четырёх, «False» –— в обратном случае.



def body_func(number: int) -> bool:
    x = float(number)
    while x >= 1:
        if x == 1:
            return True
        elif x % 4 == 0:
            x = x / 4
        else:
            return False
    return True


def read_input() -> int:
    number = int(input().strip())
    return number


print(body_func(read_input()))
