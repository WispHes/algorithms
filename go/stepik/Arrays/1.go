На первом этапе на стандартный ввод подается 10 целых положительных чисел, которые должны быть записаны в порядке ввода в массив из 10 элементов. 
Тип чисел, входящих в массив, должен соответствовать минимально возможному целому беззнаковому числу. 
Имя массива который вы должны сами создать workArray (условие обязательное). Для чтения из стандартного ввода уже импортирован пакет fmt.

На втором этапе на стандартный ввод подаются еще 3 пары чисел - индексы элементов этого массива, 
которые требуется поменять местами (если такая пара чисел 3 и 7, 
значит в массиве элемент с 3 индексом нужно поменять местами с элементом, индекс которого 7).


package main

import "fmt"

func main() {
	var (
		workArray [10]uint8
		index1    int
		index2    int
	)
	for i := 0; i < len(workArray); i++ {
		fmt.Scan(&workArray[i])
	}
	for j := 0; j < 3; j++ {
		fmt.Scan(&index1, &index2)
		workArray[index1], workArray[index2] = workArray[index2], workArray[index1]
	}

	for _, elem := range workArray {
		fmt.Print(elem, " ")
	}
}
