Рита и Гоша играют в игру. У Риты есть n фишек, на каждой из которых написано количество очков. 
Сначала Гоша называет число k, затем Рита должна выбрать две фишки, сумма очков на которых равна заданному числу.

Рите надоело искать фишки самой, и она решила применить свои навыки программирования для решения этой задачи. 
Помогите ей написать программу для поиска нужных фишек.

Формат ввода
В первой строке записано количество фишек n, 2 ≤ n ≤ 104.

Во второй строке записано n целых чисел —– очки на фишках Риты в диапазоне от -105 до 105.

В третьей строке —– загаданное Гошей целое число k, -105 ≤ k ≤ 105.

Формат вывода
Нужно вывести два числа —– очки на двух фишках, в сумме дающие k.

Если таких пар несколько, то можно вывести любую из них.

Если таких пар не существует, то вывести «None».




def two_items(items, true_item):
    for left in range(0, len(items)):
        for rigth in range(left+1, len(items)):
            if items[left] + items[rigth] == true_item:
                return items[left], items[rigth]

    return 'None',


if __name__ == '__main__':
    _ = int(input())
    print(
        *two_items(
            [int(item) for item in input().split()],
            int(input())
        )
    )
