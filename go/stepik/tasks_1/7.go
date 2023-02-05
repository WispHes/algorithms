Количество нулей
По данным числам, определите количество чисел, которые равны нулю.  

Входные данные 
Вводится натуральное число N, а затем N чисел.

Выходные данные 
Выведите количество чисел, которые равны нулю


package main

import "fmt"

func main() {
	var countItems, counter int
	fmt.Scan(&countItems)
	for ; countItems > 0; countItems-- {
		var item int
		fmt.Scan(&item)
		if item == 0 {
			counter++
		}
	}
	fmt.Print(counter)
}
