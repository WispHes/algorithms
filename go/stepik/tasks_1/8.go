Количество минимумов
Найдите количество минимальных элементов в последовательности.

Входные данные
Вводится натуральное число N, а затем N целых чисел последовательности.

Выходные данные
Выведите количество минимальных элементов последовательности.


package main

import "fmt"

func main() {
	var countItems, min, item, counter int
	fmt.Scan(&countItems, &item)
	min, counter = item, 1
	for i := 1; i < countItems; i++ {
		fmt.Scan(&item)
		if min > item {
			min, counter = item, 1
		} else if item == min {
			counter++
		}
	}
	fmt.Println(counter)
}
