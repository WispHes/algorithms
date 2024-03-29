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


def fun_values(items: List[int]) -> int:
    degree = 2
    return (
        items[0]*items[1]**degree+items[2]*items[1]+items[3]
    )


if __name__ == '__main__':
    print(fun_values([int(item) for item in input().split()]))
