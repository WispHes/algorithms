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
