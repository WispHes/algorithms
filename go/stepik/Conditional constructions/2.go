По данному трехзначному числу определите, все ли его цифры различны.

Формат входных данных
На вход подается одно натуральное трехзначное число.

Формат выходных данных
Выведите "YES", если все цифры числа различны, в противном случае - "NO".


package main

import "fmt"

func main() {
	var item int
	fmt.Scan(&item)
	var (
		first_number  = item % 10
		second_number = (item / 10) % 10
		third_number  = item / 100
	)
	switch {
	case (first_number != second_number &&
		second_number != third_number &&
		first_number != third_number):
		fmt.Println("YES")
	default:
		fmt.Println("NO")
	}
}
