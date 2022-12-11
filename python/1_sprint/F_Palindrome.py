Помогите Васе понять, будет ли фраза палиндромом‎. Учитываются только буквы и цифры, заглавные и строчные буквы считаются одинаковыми.

Решение должно работать за O(N), где N — длина строки на входе.

Формат ввода
В единственной строке записана фраза или слово. Буквы могут быть только латинские. Длина текста не превосходит 20000 символов.

Фраза может состоять из строчных и прописных латинских букв, цифр, знаков препинания.

Формат вывода
Выведите «True», если фраза является палиндромом, и «False», если не является.


import re


def body_func(line: str) -> str:
    out = re.sub(r'[^\w\s]', '', line)
    result = ''.join(out.split())
    return result


def read_input() -> str:
    line = input().strip().lower()
    return line


def print_result(result: str) -> None:
    if result[::-1] == result:
        print(True)
    else:
        print(False)


print_result(body_func(read_input()))
