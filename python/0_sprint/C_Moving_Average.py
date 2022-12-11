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
