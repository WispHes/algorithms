По данному числу N распечатайте все целые значения степени двойки, не превосходящие N, в порядке возрастания.

Входные данные
Вводится натуральное число.

Выходные данные
Выведите ответ на задачу.


package main

import "fmt"

func main() {
	var item int
	fmt.Scan(&item)
	for i := 1; item >= i; i *= 2 {
		fmt.Print(i, " ")
	}
}
