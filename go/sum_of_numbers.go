Дан массив целых чисел A и целое число k. 
Нужно найти и вывести индексы пары чисел, сумма которых равна k. 
Если таких чисел нет, то вернуть пустой слайс. 

package main

import "fmt"

func main() {
	fmt.Println(find([]int{2, 3, 1, 4, 5, 6, 2, 3, 12, 3}, 24))
}

func find(a []int, k int) []int {
	m := make(map[int]int)
	for i, v := range a {
		if y, ok := m[k-v]; ok {
			return []int{i, y}
		}
		if _, ok := m[v]; !ok {
			m[v] = i
		}
	}
	return nil
}
