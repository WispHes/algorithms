По данному числу n закончите фразу "На лугу пасется..." 
одним из возможных продолжений: "n коров", "n корова", "n коровы", правильно склоняя слово "корова".

Входные данные
Дано число n (0<n<100).

Выходные данные
Программа должна вывести введенное число n и одно из слов (на латинице): 
korov, korova или korovy, например, 1 korova, 2 korovy, 5 korov. 
Между числом и словом должен стоять ровно один пробел.


package main

import "fmt"

func main() {
	var item int
	fmt.Scan(&item)
	switch {
	case item == 1 || item > 20 && item%10 == 1:
		fmt.Println(item, `korova`)
	case item > 1 && item < 5 || (item > 20 && item%10 > 1 && item%10 < 5):
		fmt.Println(item, `korovy`)
	default:
		fmt.Println(item, `korov`)
	}
}
