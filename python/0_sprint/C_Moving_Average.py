Вам дана статистика по числу запросов в секунду к вашему любимому рекомендательному сервису.

Измерения велись n секунд.

В секунду i поступает qi запросов.

Примените метод скользящего среднего с длиной окна k к этим данным и выведите результат.

Формат ввода
В первой строке передаётся натуральное число n, количество секунд, в течение которых велись измерения. 1 ≤ n ≤ 105

Во второй строке через пробел записаны n целых неотрицательных чисел qi, каждое лежит в диапазоне от 0 до 103.

В третьей строке записано натуральное число k (1 ≤ k ≤ n) —– окно сглаживания.

Примечание для Go:

Заметьте, что в данной задаче достаточно большой размер ввода. 
Поэтому необходимо задавать размер буфера для сканнера хотя бы 600 Кб.

Формат вывода
Выведите через пробел результат применения метода скользящего среднего к серии измерений. 
Должно быть выведено n - k + 1 элементов, каждый элемент -— вещественное (дробное) число.



from typing import List, Tuple


def moving_average(chars: List[int], win: int) -> List[float]:
    result = []
    value = sum(chars[0:win])
    result.append(value/win)
    for i in range(0, len(chars)-win):
        value -= chars[i]
        value += chars[i+win]
        result.append(value/win)
    return result


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    chars = list(map(int, input().strip().split()))
    win = int(input())
    return chars, win


chars, win = read_input()
print(' '.join(map(str, moving_average(chars, win))))
