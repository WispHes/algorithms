Даны два массива чисел длины n. 
Составьте из них один массив длины 2n, в котором числа из входных массивов чередуются (первый — второй — первый — второй — ...). 
При этом относительный порядок следования чисел из одного массива должен быть сохранён.

Формат ввода
В первой строке записано целое число n –— длина каждого из массивов, 1 ≤ n ≤ 1000.

Во второй строке записано n чисел из первого массива, через пробел.

В третьей строке –— n чисел из второго массива.

Значения всех чисел –— натуральные и не превосходят 1000.

Формат вывода
Выведите 2n чисел из объединённого массива через пробел.




from typing import List, Tuple

def zipper(a: List[int], b: List[int]) -> List[int]:
    char = []
    for i in list(zip(a,b)):
        for j in i:
            char.append(str(j))
    return char

def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b

a, b = read_input()
print(' '.join(zipper(a, b)))
