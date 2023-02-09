На вход подается целое число. Необходимо возвести в квадрат каждую цифру числа и вывести получившееся число. 

Например, у нас есть число 9119. Первая цифра - 9. 9 в квадрате - 81. 
Дальше 1. Единица в квадрате - 1. В итоге получаем 811181


package main

import (
	"fmt"
)

func main() {
	var (
		items int
		res   string
	)
	_, err := fmt.Scan(&items)
	if err == nil {
		if items != 0 {
			for items > 0 {
				res = fmt.Sprint((items%10)*(items%10)) + res
				items = items / 10
			}
		} else {
			fmt.Print(items)
		}
		fmt.Print(res)
	}
}
