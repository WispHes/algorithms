Двоичная запись
Дано натуральное число N. Выведите его представление в двоичном виде.

Входные данные
Задано единственное число N

Выходные данные
Необходимо вывести требуемое представление числа N.


package main

import "fmt"

func main() {
	var (
		item int
		a    string
	)
	fmt.Scan(&item)
	for item >= 1 {
		if item == 1 {
			a = "1" + a
			break
		} else if item%2 == 0 {
			a = "0" + a
			item = item / 2
		} else {
			a = "1" + a
			item = item / 2
		}
	}
	fmt.Print(a)
}
