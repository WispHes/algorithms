Тимофей ищет место, чтобы построить себе дом. 
Улица, на которой он хочет жить, имеет длину n, то есть состоит из n одинаковых идущих подряд участков. 
Каждый участок либо пустой, либо на нём уже построен дом.

Общительный Тимофей не хочет жить далеко от других людей на этой улице. 
Поэтому ему важно для каждого участка знать расстояние до ближайшего пустого участка. 
Если участок пустой, эта величина будет равна нулю — расстояние до самого себя.

Помогите Тимофею посчитать искомые расстояния. Для этого у вас есть карта улицы. 
Дома в городе Тимофея нумеровались в том порядке, в котором строились, поэтому их номера на карте никак не упорядочены. 
Пустые участки обозначены нулями.

Формат ввода
В первой строке дана длина улицы —– n (1 ≤ n ≤ 106). 
В следующей строке записаны n целых неотрицательных чисел — номера домов и обозначения пустых участков на карте (нули). 
Гарантируется, что в последовательности есть хотя бы один ноль. Номера домов (положительные числа) уникальны и не превосходят 109.

Формат вывода
Для каждого из участков выведите расстояние до ближайшего нуля. Числа выводите в одну строку, разделяя их пробелами.



from typing import List
 

def near_zero(house_numbers: List[str]) -> List[int]:
    result = [0] * len(house_numbers)
    zero_house: List[int] = [
        index_house
        for index_house, house in enumerate(house_numbers)
        if house == '0'
    ]
    for index in range(zero_house[0]):
        result[index] = zero_house[0] - index
    for index in range(len(zero_house) - 1):
        for pos in range(zero_house[index] + 1, zero_house[index + 1]):
            result[pos] = min(pos - zero_house[index],
                              zero_house[index + 1] - pos)
    for index in range(zero_house[-1] + 1, len(house_numbers)):
        result[index] = index - zero_house[-1]
 
    return result
 

if __name__ == '__main__':
    # 79434209

    _ = int(input())
    house_numbers = input().split()
    print(*near_zero(house_numbers))

