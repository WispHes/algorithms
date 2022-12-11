Вася делает тест по математике: вычисляет значение функций в различных точках. 
Стоит отличная погода, и друзья зовут Васю гулять.
Но мальчик решил сначала закончить тест и только после этого идти к друзьям. К сожалению, Вася пока не умеет программировать.
Зато вы умеете. Помогите Васе написать код функции, вычисляющей y = ax2 + bx + c.
Напишите программу, которая будет по коэффициентам a, b, c и числу x выводить значение функции в точке x.

Формат ввода
На вход через пробел подаются целые числа a, x, b, c. В конце ввода находится перенос строки.

Формат вывода
Выведите одно число — значение функции в точке x.



from typing import List


def function_values(numbers: List[int]) -> int:
    a = numbers[0]
    x = numbers[1]
    b = numbers[2]
    c = numbers[3]
    y = a*x**2+b*x+c
    return y


def read_input() -> List[int]:
    numbers = list(map(int, input().strip().split()))
    return numbers


def print_result(y: int) -> None:
    print(y)


numbers = read_input()

print_result(function_values(numbers))
