Представьте себе онлайн-игру для поездки в метро: игрок нажимает на кнопку, и на экране появляются три случайных числа. 
Если все три числа оказываются одной чётности, игрок выигрывает.

Напишите программу, которая по трём числам определяет, выиграл игрок или нет.

Формат ввода
В первой строке записаны три случайных целых числа a, b и c. Числа не превосходят 109 по модулю.

Формат вывода
Выведите «WIN», если игрок выиграл, и «FAIL» в противном случае.



from typing import List


def body_func(numbers: List[int]) -> None:
    even_numbers = []
    odd_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    if len(even_numbers) == 3:
        print('WIN')
    elif len(odd_numbers) == 3:
        print('WIN')
    else:
        print('FAIL')


def read_input() -> List[int]:
    numbers = list(map(int, input().strip().split()))
    return numbers


numbers = read_input()

body_func(numbers)
