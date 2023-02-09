Дана строка, содержащая только арабские цифры. Найти и вывести наибольшую цифру.

Входные данные

Вводится строка ненулевой длины. Известно также, что длина строки не превышает 1000 знаков и строка содержит только арабские цифры.

Выходные данные

Выведите максимальную цифру, которая встречается во введенной строке.


package main

import "fmt"

func main() {
	var (
		items string
	)
	_, err := fmt.Scan(&items)
	if err == nil {
		res := items[0]
		for index := range items {
			if items[index] > res {
				res = items[index]
			}
		}
		fmt.Print(string(res))
	}
}
