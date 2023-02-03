Напишите программу, принимающая на вход число N (N \geq 4)N(N≥4), а затем NN целых чисел-элементов среза. 
На вывод нужно подать 4-ый (3 по индексу) элемент данного среза.


package main

import "fmt"

func main() {
	var (
		countItems int
		item       int
	)
	fmt.Scan(&countItems)
	a := make([]int, 0, countItems)
	for i := 0; i < countItems; i++ {
		fmt.Scan(&item)
		a = append(a, item)
	}
	fmt.Println(a[3])
}
