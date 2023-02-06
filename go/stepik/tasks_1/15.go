Из натурального числа удалить заданную цифру.

Входные данные
Вводятся натуральное число и цифра, которую нужно удалить.

Выходные данные
Вывести число без заданных цифр.


package main

import "fmt"

func main() {
	var item, num int
	var a []int
	fmt.Scan(&item, &num)
	for item != 0 {
		if item%10 != num {
			a = append(a, item%10)
		}
		item = item / 10
	}
	for i := len(a) - 1; i >= 0; i-- {
		fmt.Print(a[i])
	}
}
