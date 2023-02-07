Васе очень нравятся задачи про строки, поэтому он придумал свою. 
Есть 2 строки s и t, состоящие только из строчных букв. 
Строка t получена перемешиванием букв строки s и добавлением 1 буквы в случайную позицию. 
Нужно найти добавленную букву.

Формат ввода
На вход подаются строки s и t, разделённые переносом строки. Длины строк не превосходят 1000 символов. 
Строки не бывают пустыми.

Формат вывода
Выведите лишнюю букву.


def extra_letter(first_str, second_str):
    for char in second_str:
        if char in first_str:
            second_str = second_str.replace(char, '', 1)
            first_str = first_str.replace(char, '', 1)

    return second_str


if __name__ == '__main__':
    print(
        extra_letter(input(), input())
    )
