Представьте себе онлайн-игру для поездки в метро: игрок нажимает на кнопку, и на экране появляются три случайных числа. 
Если все три числа оказываются одной чётности, игрок выигрывает.

Напишите программу, которая по трём числам определяет, выиграл игрок или нет.

Формат ввода
В первой строке записаны три случайных целых числа a, b и c. Числа не превосходят 109 по модулю.

Формат вывода
Выведите «WIN», если игрок выиграл, и «FAIL» в противном случае.



from typing import List


def even_and_odd(items: List[int]) -> str:
    even, odd = 0, 0
    for num in items:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    if even == 3 or odd == 3:
        return 'WIN'
    return 'FAIL'


if __name__ == '__main__':
    print(even_and_odd([int(item) for item in input().split()]))
