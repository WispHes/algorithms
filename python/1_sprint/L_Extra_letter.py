Васе очень нравятся задачи про строки, поэтому он придумал свою. 
Есть 2 строки s и t, состоящие только из строчных букв. 
Строка t получена перемешиванием букв строки s и добавлением 1 буквы в случайную позицию. 
Нужно найти добавленную букву.

Формат ввода
На вход подаются строки s и t, разделённые переносом строки. Длины строк не превосходят 1000 символов. 
Строки не бывают пустыми.

Формат вывода
Выведите лишнюю букву.



from typing import List, Tuple


def body_func(first_str: List[str], second_str: List[str]) -> None:
    for i in range(0, len(second_str)):
        try:
            if second_str[i] != first_str[i]:
                print(second_str[i])
                break
        except Exception:
            print(second_str[-1])


def read_iput() -> Tuple[List[str], List[str]]:
    first_str = list(sorted(input().strip()))
    second_str = list(sorted(input().strip()))
    return first_str, second_str


first_str, second_str = read_iput()

body_func(first_str, second_str)
