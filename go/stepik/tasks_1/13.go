Номер числа Фибоначчи
Дано натуральное число A > 1. 
Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φn=A. 
Если А не является числом Фибоначчи, выведите число -1.

Входные данные
Вводится натуральное число.

Выходные данные
Выведите ответ на задачу.

package main

import "fmt"

func main() {
	var (
		item int
		i1   = 1
		i2   = 1
		c1   = 1
		c2   = 2
	)
	fmt.Scan(&item)
	if item == 0 {
		fmt.Print(0)
	} else {
		for i := 0; i <= item; i++ {
			i1, i2 = i2, i2+i1
			c1 += 1
			c2 += 1
			if i1 == item {
				fmt.Println(c1)
				break
			} else if i2 == item {
				fmt.Println(c2)
				break
			}
		}
		if i1 != item && i2 != item {
			fmt.Println(-1)
		}
	}
}
