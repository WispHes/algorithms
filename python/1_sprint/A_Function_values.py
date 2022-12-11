from typing import List


def function_values(numbers: List[int]) -> int:
    a = numbers[0]
    x = numbers[1]
    b = numbers[2]
    c = numbers[3]
    y = a*x**2+b*x+c
    return y


def read_input() -> List[int]:
    numbers = list(map(int, input().strip().split()))
    return numbers


def print_result(y: int) -> None:
    print(y)


numbers = read_input()

print_result(function_values(numbers))
