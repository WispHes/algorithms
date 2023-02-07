Тимофей записал два числа в двоичной системе счисления и попросил Гошу вывести их сумму, также в двоичной системе. 
Встроенную в язык программирования возможность сложения двоичных чисел применять нельзя. Помогите Гоше решить задачу.

Решение должно работать за O(N), где N –— количество разрядов максимального числа на входе.

Формат ввода
Два числа в двоичной системе счисления, каждое на отдельной строке. Длина каждого числа не превосходит 10 000 символов.

Формат вывода
Одно число в двоичной системе счисления.


def binary_system(left, right):
    zero, one, two = 0, 1, 2
    len_left = len(left)
    len_right = len(right)
    max_len = max(len_left, len_right)
    left += [0] * (max_len - len_left)
    right += [0] * (max_len - len_right)
    ans = []
    queue = 0
    for index in range(max_len):
        if left[index] + right[index] + queue == zero:
            ans.append('0')
        elif left[index] + right[index] + queue == one:
            ans.append('1')
            queue = 0
        elif left[index] + right[index] == two and queue == one:
            queue = 0
            ans.append('1')
            queue += 1
        elif left[index] + right[index] + queue == two:
            queue = 0
            ans.append('0')
            queue += 1
    if queue > 0:
        ans.append('1')
    print(''.join(ans[::-1]))


if __name__ == '__main__':
    x = [int(item) for item in input()]
    y = [int(item) for item in input()]
    binary_system(x[::-1], y[::-1])
