Дана матрица. Нужно написать функцию, которая для элемента возвращает всех его соседей. 
Соседним считается элемент, находящийся от текущего на одну ячейку влево, вправо, вверх или вниз. 
Диагональные элементы соседними не считаются.

Например, в матрице A соседними элементами для (0, 0) будут 2 и 0. А для (2, 1) –— 1, 2, 7, 7.

Формат ввода
В первой строке задано n — количество строк матрицы. Во второй — количество столбцов m. 
Числа m и n не превосходят 1000. В следующих n строках задана матрица. 
Элементы матрицы — целые числа, по модулю не превосходящие 1000.
В последних двух строках записаны координаты элемента, соседей которого нужно найти. Индексация начинается с нуля.

Формат вывода
Напечатайте нужные числа в возрастающем порядке через пробел.


from typing import List, Union


def neighbors(
    arr: List[List[str]],
    os_y: int,
    os_x: int,
    y_len: int,
    x_len: int
) -> Union[List[int], str]:
    result = []
    if os_y + 1 <= y_len:
        result.append(int(arr[os_y+1][os_x]))
    if os_y - 1 >= 0:
        result.append(int(arr[os_y-1][os_x]))
    if os_x + 1 <= x_len:
        result.append(int(arr[os_y][os_x+1]))
    if os_x - 1 >= 0:
        result.append(int(arr[os_y][os_x-1]))

    return sorted(result)


if __name__ == '__main__':
    try:
        y_len = int(input())
        x_len = int(input())
        print(
            *neighbors(
                [input().split() for _ in range(y_len)],
                int(input()),
                int(input()),
                y_len-1,
                x_len-1
            )
        )
    except Exception:
        print('')
