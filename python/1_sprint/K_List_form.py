Вася просил Аллу помочь решить задачу. На этот раз по информатике.

Для неотрицательного целого числа X списочная форма –— это массив его цифр слева направо. 
К примеру, для 1231 списочная форма будет [1,2,3,1]. 
На вход подается количество цифр числа Х, списочная форма неотрицательного числа Х и неотрицательное число K. 
Числа К и Х не превосходят 10000.

Нужно вернуть списочную форму числа X + K.

Формат ввода
В первой строке — длина списочной формы числа X. 
На следующей строке — сама списочная форма с цифрами записанными через пробел.

В последней строке записано число K, 0 ≤ K ≤ 10000.

Формат вывода
Выведите списочную форму числа X+K.



from typing import Tuple


def body_func(number_list: int, k: int) -> str:
    result = number_list + k
    return str(result)


def read_input() -> Tuple[int, int]:
    n = int(input())
    number_list = int(''.join(input().strip().split()))
    k = int(input())
    return number_list, k


def print_result(result: str) -> None:
    print(' '.join(list(result)))


number_list, k = read_input()

print_result(body_func(number_list, k))
